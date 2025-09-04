import requests

url = "http://sinalprivado.info:80/movie/632035/GqGcFV4ntu/655644.mp4"
nome_arquivo = "filme.mp4"

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

# Verifica se o retorno realmente é vídeo
print("Content-Type:", response.headers.get("Content-Type"))

if "video" not in response.headers.get("Content-Type", ""):
    print("⚠️ O servidor não está entregando o vídeo. Pode ser necessário login/token.")
else:
    with open(nome_arquivo, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"✅ Download concluído: {nome_arquivo}")
