import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/V6UF18WPgCgx1sqisQJIYw==,1766844987/videos/hls/41/57/ab/4157ab7c45a6ca3d0b83b0e20caca39f/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)