import yt_dlp

def baixar_video(url, caminho_destino):
    opcoes = {
        'format': 'mp4',  # Especifica o formato como MP4
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Define o caminho de destino e o nome do arquivo
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

# Exemplo de uso
url_video = 'https://youtu.be/zx0C23HTN5Q?si=gmsiU69jZEHAjSiM'
caminho_destino = 'D:/baixarm3u8/'  # Defina o caminho onde quer salvar o vídeo
baixar_video(url_video, caminho_destino)
