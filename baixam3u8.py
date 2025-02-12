import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/u1ZVnSQp6R5BHBSXrLN8YA==,1739393330/videos/hls/28/79/30/287930f4c11433fc82c0bf7138f3877e/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)