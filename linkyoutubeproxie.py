import requests
import subprocess
import time

# URL da live do YouTube
youtube_url = "https://www.youtube.com/live/ohxP6CBImKI"

# Obtendo uma lista de proxies brasileiros gratuitos
proxy_api = "https://www.proxy-list.download/api/v1/get?type=http&country=BR"
response = requests.get(proxy_api)

if response.status_code == 200:
    proxy_list = response.text.strip().split("\r\n")
    max_attempts = 10  # Número máximo de proxies a serem testados
    attempt_count = 0  # Contador de tentativas

    for proxy in proxy_list:
        if attempt_count >= max_attempts:
            print("Número máximo de tentativas atingido. Nenhum proxy válido encontrado.")
            break

        proxy_url = f"http://{proxy}"
        print(f"Tentando proxy brasileiro: {proxy}")

        # Testa o proxy antes de usar
        try:
            test_response = requests.get("http://www.google.com", proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
            if test_response.status_code == 200:
                print(f"Proxy funcionando: {proxy}")

                # Executando o yt-dlp com proxy válido
                command = ["yt-dlp", "--proxy", proxy_url, "-g", youtube_url]

                try:
                    result = subprocess.run(command, capture_output=True, text=True, check=True, timeout=15)
                    stream_url = result.stdout.strip()
                    if stream_url:
                        print(f"✅ Link do stream: {stream_url}")
                        break  # Para a busca ao encontrar um proxy válido
                except subprocess.CalledProcessError as e:
                    print("⚠️ Erro ao obter o link do stream:", e.stderr)
                except subprocess.TimeoutExpired:
                    print("⏳ O yt-dlp demorou muito para responder. Tentando outro proxy...")
            else:
                print(f"❌ Proxy {proxy} falhou no teste.")
        except requests.RequestException:
            print(f"❌ Proxy {proxy} não respondeu. Tentando outro...")

        attempt_count += 1
        time.sleep(2)  # Pequeno intervalo entre os testes

else:
    print("⚠️ Falha ao obter proxies.")
