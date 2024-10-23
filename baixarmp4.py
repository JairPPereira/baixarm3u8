import wget

def download_file(url):
    try:
        print(f"Iniciando o download do arquivo: {url}")
        filename = wget.download(url)  # Baixa e salva o arquivo no diretório atual
        print(f"\nDownload completo! Arquivo salvo como: {filename}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
file_url = input("http://lvroku.live:80/movie/p2pLinha/live1763675801/220954.mp4")
download_file(file_url)