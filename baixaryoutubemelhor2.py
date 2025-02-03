import yt_dlp

def baixar_video(url, caminho_destino):
    opcoes = {
        'format': 'bestvideo/best',  # Baixa a melhor qualidade de vídeo e áudio combinados
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Define o caminho de destino e o nome do arquivo
        'merge_output_format': 'mp4',  # Força o formato final como MP4
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

# Exemplo de uso
url_video = 'https://youtu.be/rWJIunolRHk?si=BVKYUhT1_1U_-CVJ'
caminho_destino = 'D:/baixarm3u8/'  # Defina o caminho onde quer salvar o vídeo
baixar_video(url_video, caminho_destino)