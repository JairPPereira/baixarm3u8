import ffmpeg

# Caminho do vídeo original
video_input = "video.mp4"

# Caminho do vídeo recortado
video_output = "video_cortado.mp4"

# Tempo de início e fim do corte (em segundos)
start_time = 7  # Exemplo: Iniciar no segundo 10
end_time = 33    # Exemplo: Terminar no segundo 20

# Comando para cortar o vídeo
ffmpeg.input(video_input, ss=start_time, to=end_time).output(video_output).run()

print("Vídeo cortado com sucesso!")
