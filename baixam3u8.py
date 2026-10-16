import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://hls-cdn77.xvideos-cdn.com/cHMYUyz63bjceZ-2vQeLrg==,1792160377/d09e9387-3e19-4c9a-9091-85102c953d7c/0/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)