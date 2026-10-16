# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import threading
import time
import tkinter as tk

from tkinter import ttk, filedialog, messagebox
from pathlib import Path


# ============================================
# CONFIGURAÇÃO DO FFMPEG
# ============================================

FFMPEG_DIR = (
    r"C:\Users\jairp\AppData\Local"
    r"\Microsoft\WinGet\Links"
)

os.environ["PATH"] = (
    FFMPEG_DIR
    + os.pathsep
    + os.environ.get("PATH", "")
)

FFMPEG = shutil.which("ffmpeg")
FFPROBE = shutil.which("ffprobe")


# ============================================
# INTERFACE PRINCIPAL
# ============================================

class M3U8Downloader:

    def __init__(self, root):

        self.root = root
        self.root.title("JP M3U8 Downloader")
        self.root.geometry("720x530")
        self.root.minsize(620, 480)

        self.processo = None
        self.baixando = False
        self.cancelado = False
        self.inicio = None

        self.url = tk.StringVar()
        self.pasta = tk.StringVar(
            value=str(Path.home() / "Downloads")
        )
        self.nome = tk.StringVar(value="video.mp4")

        self.status = tk.StringVar(value="Aguardando download")
        self.velocidade = tk.StringVar(value="Velocidade: --")
        self.tempo = tk.StringVar(value="Tempo restante: --")
        self.progresso = tk.DoubleVar(value=0)

        self.criar_interface()

    # ========================================
    # CONSTRUÇÃO DA INTERFACE
    # ========================================

    def criar_interface(self):

        frame = ttk.Frame(self.root, padding=20)
        frame.pack(fill="both", expand=True)

        titulo = ttk.Label(
            frame,
            text="JP M3U8 Downloader",
            font=("Segoe UI", 20, "bold")
        )
        titulo.pack(pady=(0, 10))

        subtitulo = ttk.Label(
            frame,
            text="Download de transmissões HLS para MP4",
            font=("Segoe UI", 10)
        )
        subtitulo.pack(pady=(0, 20))

        ttk.Label(
            frame,
            text="URL do vídeo M3U8:"
        ).pack(anchor="w")

        ttk.Entry(
            frame,
            textvariable=self.url
        ).pack(fill="x", pady=5)

        ttk.Label(
            frame,
            text="Nome do arquivo:"
        ).pack(anchor="w", pady=(10, 0))

        ttk.Entry(
            frame,
            textvariable=self.nome
        ).pack(fill="x", pady=5)

        ttk.Label(
            frame,
            text="Pasta de destino:"
        ).pack(anchor="w", pady=(10, 0))

        pasta_frame = ttk.Frame(frame)
        pasta_frame.pack(fill="x", pady=5)

        ttk.Entry(
            pasta_frame,
            textvariable=self.pasta
        ).pack(
            side="left",
            fill="x",
            expand=True
        )

        ttk.Button(
            pasta_frame,
            text="Procurar",
            command=self.escolher_pasta
        ).pack(side="left", padx=5)

        self.barra = ttk.Progressbar(
            frame,
            variable=self.progresso,
            maximum=100,
            mode="determinate"
        )
        self.barra.pack(
            fill="x",
            pady=(25, 10)
        )

        ttk.Label(
            frame,
            textvariable=self.status
        ).pack()

        ttk.Label(
            frame,
            textvariable=self.velocidade
        ).pack(pady=5)

        ttk.Label(
            frame,
            textvariable=self.tempo
        ).pack()

        botoes = ttk.Frame(frame)
        botoes.pack(pady=20)

        self.botao_baixar = ttk.Button(
            botoes,
            text="▶ Baixar vídeo",
            command=self.iniciar_download
        )
        self.botao_baixar.pack(
            side="left",
            padx=10
        )

        self.botao_cancelar = ttk.Button(
            botoes,
            text="■ Cancelar",
            command=self.cancelar_download,
            state="disabled"
        )
        self.botao_cancelar.pack(
            side="left",
            padx=10
        )

        ttk.Label(
            frame,
            text="Registro de atividades:"
        ).pack(anchor="w")

        self.log = tk.Text(
            frame,
            height=6,
            wrap="word",
            state="disabled"
        )
        self.log.pack(
            fill="both",
            expand=True,
            pady=5
        )

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.fechar
        )

    # ========================================
    # FUNÇÕES AUXILIARES
    # ========================================

    def escrever_log(self, mensagem):

        def atualizar():

            self.log.configure(state="normal")
            self.log.insert("end", mensagem + "\n")
            self.log.see("end")
            self.log.configure(state="disabled")

        self.root.after(0, atualizar)

    def atualizar_status(self, texto):

        self.root.after(
            0,
            lambda: self.status.set(texto)
        )

    def escolher_pasta(self):

        pasta = filedialog.askdirectory()

        if pasta:
            self.pasta.set(pasta)

    def formatar_tempo(self, segundos):

        segundos = max(0, int(segundos))

        horas, resto = divmod(segundos, 3600)
        minutos, segundos = divmod(resto, 60)

        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    def obter_duracao(self, url):

        if not FFPROBE:
            return None

        comando = [
            FFPROBE,
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            url
        ]

        try:

            resultado = subprocess.run(
                comando,
                capture_output=True,
                text=True,
                timeout=20
            )

            duracao = float(resultado.stdout.strip())

            if duracao > 0:
                return duracao

        except (ValueError, OSError, subprocess.TimeoutExpired):
            pass

        return None

    # ========================================
    # INICIAR DOWNLOAD
    # ========================================

    def iniciar_download(self):

        if self.baixando:
            return

        url = self.url.get().strip()
        pasta = self.pasta.get().strip()
        nome = self.nome.get().strip()

        if not url.startswith(("http://", "https://")):

            messagebox.showerror(
                "Erro",
                "Informe uma URL HTTP ou HTTPS válida."
            )
            return

        if not nome:
            messagebox.showerror(
                "Erro",
                "Informe o nome do arquivo."
            )
            return

        nome = os.path.basename(nome)

        if not nome.lower().endswith(".mp4"):
            nome += ".mp4"

        if not os.path.isdir(pasta):

            messagebox.showerror(
                "Erro",
                "A pasta de destino não existe."
            )
            return

        if not FFMPEG:

            messagebox.showerror(
                "Erro",
                "FFmpeg não encontrado."
            )
            return

        destino = os.path.join(pasta, nome)

        if os.path.exists(destino):

            messagebox.showerror(
                "Arquivo existente",
                "Já existe um arquivo com esse nome."
            )
            return

        self.baixando = True
        self.cancelado = False
        self.inicio = time.monotonic()

        self.progresso.set(0)
        self.velocidade.set("Velocidade: --")
        self.tempo.set("Tempo restante: --")

        self.botao_baixar.configure(state="disabled")
        self.botao_cancelar.configure(state="normal")

        self.escrever_log("Iniciando download...")
        self.escrever_log(f"Destino: {destino}")

        thread = threading.Thread(
            target=self.executar_download,
            args=(url, destino),
            daemon=True
        )

        thread.start()

    # ========================================
    # EXECUTAR FFMPEG
    # ========================================

    def executar_download(self, url, destino):

        duracao = self.obter_duracao(url)

        if self.cancelado:
            self.finalizar(False, "Download cancelado.")
            return

        if duracao:
            self.escrever_log(
                f"Duração: {self.formatar_tempo(duracao)}"
            )
        else:
            self.escrever_log(
                "Duração desconhecida. Progresso indeterminado."
            )

        comando = [
            FFMPEG,
            "-hide_banner",
            "-loglevel", "error",
            "-nostdin",
            "-i", url,
            "-c", "copy",
            "-progress", "pipe:1",
            "-nostats",
            destino
        ]

        try:

            self.atualizar_status("Baixando vídeo...")

            self.processo = subprocess.Popen(
                comando,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                errors="replace",
                creationflags=subprocess.CREATE_NO_WINDOW
            )

            # Ler erros em paralelo para evitar
            # bloqueio dos buffers do processo.

            erros = []

            def ler_erros():

                for linha in self.processo.stderr:
                    erros.append(linha)

            thread_erros = threading.Thread(
                target=ler_erros,
                daemon=True
            )
            thread_erros.start()

            for linha in self.processo.stdout:

                if self.cancelado:
                    break

                linha = linha.strip()

                if linha.startswith("out_time="):

                    tempo_video = linha.split("=", 1)[1]

                    try:

                        partes = tempo_video.split(":")
                        segundos = (
                            float(partes[0]) * 3600
                            + float(partes[1]) * 60
                            + float(partes[2])
                        )

                        if duracao:

                            percentual = min(
                                99.9,
                                segundos / duracao * 100
                            )

                            decorrido = (
                                time.monotonic() - self.inicio
                            )

                            restante = 0

                            if percentual > 0:

                                restante = (
                                    decorrido
                                    * (100 - percentual)
                                    / percentual
                                )

                            self.root.after(
                                0,
                                lambda p=percentual:
                                self.progresso.set(p)
                            )

                            texto = (
                                "Tempo restante: "
                                + self.formatar_tempo(restante)
                            )

                            self.root.after(
                                0,
                                lambda t=texto:
                                self.tempo.set(t)
                            )

                    except (ValueError, IndexError):
                        pass

                elif linha.startswith("speed="):

                    velocidade = linha.split("=", 1)[1]

                    self.root.after(
                        0,
                        lambda v=velocidade:
                        self.velocidade.set(
                            f"Velocidade de processamento: {v}"
                        )
                    )

            codigo = self.processo.wait()
            thread_erros.join(timeout=2)

            if self.cancelado:

                self.finalizar(
                    False,
                    "Download cancelado."
                )
                return

            if codigo != 0:

                mensagem = "".join(erros).strip()

                if not mensagem:
                    mensagem = f"FFmpeg retornou código {codigo}."

                self.escrever_log(mensagem)

                self.finalizar(
                    False,
                    "Erro ao baixar o vídeo."
                )
                return

            if not os.path.isfile(destino):

                self.finalizar(
                    False,
                    "O arquivo MP4 não foi criado."
                )
                return

            if os.path.getsize(destino) == 0:

                self.finalizar(
                    False,
                    "O arquivo MP4 está vazio."
                )
                return

            self.finalizar(
                True,
                f"Download concluído!\n{destino}"
            )

        except Exception as erro:

            self.escrever_log(str(erro))

            self.finalizar(
                False,
                f"Erro: {erro}"
            )

        finally:
            self.processo = None

    # ========================================
    # FINALIZAÇÃO
    # ========================================

    def finalizar(self, sucesso, mensagem):

        def atualizar():

            self.baixando = False

            self.botao_baixar.configure(
                state="normal"
            )

            self.botao_cancelar.configure(
                state="disabled"
            )

            if sucesso:

                self.progresso.set(100)
                self.status.set("Concluído!")

                messagebox.showinfo(
                    "Sucesso",
                    mensagem
                )

            else:

                self.status.set(mensagem)

                if not self.cancelado:
                    messagebox.showerror(
                        "Erro",
                        mensagem
                    )

            self.escrever_log(mensagem)

        self.root.after(0, atualizar)

    # ========================================
    # CANCELAMENTO
    # ========================================

    def cancelar_download(self):

        if not self.baixando:
            return

        self.cancelado = True

        self.status.set("Cancelando...")

        if self.processo:

            try:
                self.processo.terminate()
            except OSError:
                pass

    def fechar(self):

        if self.baixando:

            resposta = messagebox.askyesno(
                "Sair",
                "Existe um download em andamento. Deseja sair?"
            )

            if not resposta:
                return

            self.cancelado = True

            if self.processo:

                try:
                    self.processo.terminate()
                except OSError:
                    pass

        self.root.destroy()


# ============================================
# EXECUÇÃO
# ============================================

if __name__ == "__main__":

    root = tk.Tk()

    app = M3U8Downloader(root)

    root.mainloop()