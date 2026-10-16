import os
import shutil
import subprocess

# Caminho onde o Winget disponibiliza o FFmpeg
FFMPEG_DIR = r"C:\Users\jairp\AppData\Local\Microsoft\WinGet\Links"

# Adicionar FFmpeg ao PATH do processo Python
os.environ["PATH"] = FFMPEG_DIR + os.pathsep + os.environ.get("PATH", "")

# Verificar executáveis
for programa in ["ffmpeg", "ffprobe", "ffplay"]:
    caminho = shutil.which(programa)
    print(f"{programa}: {caminho}")

# Verificar se FFmpeg funciona
ffmpeg = shutil.which("ffmpeg")

if not ffmpeg:
    raise RuntimeError("FFmpeg não encontrado!")

resultado = subprocess.run(
    [ffmpeg, "-version"],
    capture_output=True,
    text=True
)

print(resultado.stdout.splitlines()[0])

# Importar biblioteca somente após configurar o PATH
import m3u8_To_MP4

if __name__ == "__main__":

    m3u8_url = "https://hls-cdn77.xvideos-cdn.com/cHMYUyz63bjceZ-2vQeLrg==,1792160377/d09e9387-3e19-4c9a-9091-85102c953d7c/0/hls.m3u8"

    m3u8_To_MP4.multithread_download(m3u8_url)