from moviepy.editor import AudioFileClip, ImageClip

# Caminhos dos arquivos
imagem = "imagem.jpg"       # imagem que será mostrada no vídeo
audio = "audio.mp3"         # seu arquivo de áudio (pode ser .mp3 ou .wav)
saida = "saida_video.mp4"   # nome do vídeo final

# Carrega o áudio
audio_clip = AudioFileClip(audio)

# Cria um vídeo com a imagem fixa e mesma duração do áudio
video_clip = ImageClip(imagem, duration=audio_clip.duration)
video_clip = video_clip.set_audio(audio_clip)
video_clip = video_clip.set_duration(audio_clip.duration)
video_clip = video_clip.set_fps(1)  # 1 frame por segundo (imagem fixa)

# Exporta o vídeo com áudio em 192 kbps
video_clip.write_videofile(
    saida,
    codec="libx264",             # Codec de vídeo
    audio_codec="aac",           # Codec de áudio
    audio_bitrate="192k"         # Qualidade de áudio especificada (192 kbps)
)
