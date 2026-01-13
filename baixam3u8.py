import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://hls-cdn77.xvideos-cdn.com/hzfyZi8Qw5e7P-rLKKjlAA==,1768307544/1dad8c5c-9051-4f28-94e1-1cb9e4ca06b9/3/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)