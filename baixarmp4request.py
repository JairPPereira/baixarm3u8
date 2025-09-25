import requests
import sys

url = "http://sinalprivado.info:80/movie/632035/GqGcFV4ntu/884362.mp4"
nome_arquivo = "884362.mp4"

# Cabeçalhos simulando navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Connection": "keep-alive",
}

print(f"⬇️ Baixando {url}...")

response = requests.get(url, headers=headers, stream=True, allow_redirects=True)
total_length = response.headers.get('content-length')

if total_length is None:
    print("⚠️ Não foi possível obter o tamanho do arquivo.")
    total_length = 0
else:
    total_length = int(total_length)

baixado = 0
with open(nome_arquivo, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)
            baixado += len(chunk)
            if total_length:
                done = int(50 * baixado / total_length)  # 50 = tamanho da barra
                sys.stdout.write(
                    f"\r[{'=' * done}{' ' * (50-done)}] "
                    f"{baixado / 1024 / 1024:.2f} MB / {total_length / 1024 / 1024:.2f} MB"
                )
                sys.stdout.flush()

print(f"\n✅ Download concluído: {nome_arquivo}")
