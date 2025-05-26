import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/4KIwRDyiEvkKjWo8XEqfyA==,1748269683/videos/hls/eb/c2/bb/ebc2bb6b4d311068d14308bb81c9c67b/hls-1080p-47230.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)