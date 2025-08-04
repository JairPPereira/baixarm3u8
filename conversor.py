import ffmpeg

input_audio = 'audio.mp3'
input_image = 'imagem.jpg'
output_video = 'saida_video.mp4'

(
    ffmpeg
    .input(input_image, loop=1, framerate=1)
    .output(input_audio, output_video, 
            vcodec='libx264', 
            acodec='aac', 
            audio_bitrate='192k', 
            shortest=None, 
            pix_fmt='yuv420p')
    .run()
)
