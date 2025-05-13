import yt_dlp

def baixar_video(url, caminho_destino):
    opcoes = {
        'format': 'mp4',  # Especifica o formato como MP4
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Define o caminho de destino e o nome do arquivo
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

# Exemplo de uso
url_video = 'https://cdn77-vid.xvideos-cdn.com/41HkfGtZEf7EeMWu7Ik9zw==,1747144049/videos/hls/8e/8e/9d/8e8e9da672e976265bdbccc95cfcc3c3/hls-720p.m3u8'
caminho_destino = 'D:/baixarm3u8/'  # Defina o caminho onde quer salvar o vídeo
baixar_video(url_video, caminho_destino)
