import subprocess

def corrigir_audio(video_path, output_path):
    try:
        # Comando FFmpeg para reprocessar áudio
        comando = [
            "ffmpeg",
            "-i", video_path,  # Entrada
            "-c:v", "copy",  # Copiar o vídeo sem recodificar
            "-c:a", "aac",  # Reprocessar o áudio para AAC
            output_path  # Arquivo de saída
        ]
        # Executar o comando
        subprocess.run(comando, check=True)
        print(f"Vídeo corrigido salvo em: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao corrigir o áudio: {e}")

# Exemplo de uso
corrigir_audio("video_corrompido.mp4", "video_corrigido.mp4")
