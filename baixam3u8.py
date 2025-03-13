import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/HaXfz3Gk88Cgr7cs8Btipw==,1741369109/videos/hls/3f/94/b8/3f94b86a445de99d54a0d77d1c1b238f-1/hls-720p.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)