import subprocess

input_audio = 'passado1.mp3'
input_image = 'JPMUSIC.png'
output_video = 'saida_video.mp4'

cmd = [
    'ffmpeg',
    '-loop', '1',
    '-i', input_image,
    '-i', input_audio,
    '-c:v', 'libx264',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-shortest',
    '-pix_fmt', 'yuv420p',
    output_video
]

subprocess.run(cmd, check=True)
