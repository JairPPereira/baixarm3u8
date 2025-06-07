import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/29VAT1FPmkYQ4Pg2ksj8og==,1749338300/videos/hls/f6/e1/fe/f6e1fe95d4db604f220cf6097116de31/hls-1080p-89b01.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)