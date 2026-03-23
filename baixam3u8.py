import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://hls-cdn77.xvideos-cdn.com/2OUKXcjIFpeGluLvVyH1-w==,1774293370/43e08f10-0694-4dd0-a21a-8e4e9f9bd8a1/3/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)