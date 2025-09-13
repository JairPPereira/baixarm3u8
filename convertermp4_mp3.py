import subprocess
import os

def mp4_to_mp3(input_file, output_file=None):
    if output_file is None:
        base, _ = os.path.splitext(input_file)
        output_file = base + ".mp3"
    
    # Comando FFmpeg para extrair áudio em 320 kbps
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vn",                # ignora vídeo
        "-ar", "44100",       # frequência padrão de CD
        "-ac", "2",           # áudio estéreo
        "-b:a", "320k",       # qualidade 320 kbps
        output_file,
        "-y"                  # sobrescreve se já existir
    ]
    
    subprocess.run(command, check=True)
    print(f"✅ Conversão concluída: {output_file}")

# Exemplo de uso:
mp4_to_mp3("Terra_seca.mp4", "Terra_seca.mp3")
