import yt_dlp

def baixar_video(url, caminho_destino):
    opcoes = {
        'format': 'mp4',  # Especifica o formato como MP4
        'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Define o caminho de destino e o nome do arquivo
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

# Exemplo de uso
url_video = 'https://pipocadesal5.store/movie/mousasticoshvily/mrtv15xx/320716.mp4?token=TxRaWEpeRw5HUVoCBglYBAgHAVpUXFcNAlBRAVIFX1BVBQAADg4HAgQVFURDTEtUUQ49UFNGDgcABQMDVE9EREdTQGZQUkcORwYNVQYBDhMcQRZQWgEWDgMCAAZUV1AABg8eG0lfARZfFQtWCAsPExxBB0FDAUZaU1lrVgcVD1JRFAgbGxpHWwtoXQNdWVdVEllACRVIFl1BRRYIDBYKXRgUUFBNRARAABUDRAgKChMcQQFWQgpARksXDhA3MEQdFlNKTVxYFl0KWRtcElVJBRJPQFBEO0ZRQUFGVwMOA0MWDBAJGxpHWQRPZgVfVldUUxcLVlkXFg4QBhYeQA4JX11CXUtmRgxQRw1XE1xURA=='
caminho_destino = 'D:/baixarm3u8/'  # Defina o caminho onde quer salvar o vídeo
baixar_video(url_video, caminho_destino)
