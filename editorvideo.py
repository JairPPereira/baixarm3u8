from moviepy.editor import VideoFileClip

# Caminho do vídeo de entrada
video_path = "video.mp4"  # Substitua pelo caminho do seu vídeo

# Tempo de início e fim do corte (em segundos)
start_time = 10  # Início aos 10 segundos
end_time = 20    # Fim aos 20 segundos

# Carrega o vídeo
video = VideoFileClip(video_path)

# Recorta o trecho desejado
video_recortado = video.subclip(start_time, end_time)

# Salva o novo vídeo
video_recortado.write_videofile("video_cortado.mp4", codec="libx264", fps=30)

print("Vídeo recortado salvo como 'video_cortado.mp4'")
