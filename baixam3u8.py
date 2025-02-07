import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://gcore-vid.xvideos-cdn.com/-s69OR1_bjyQdhdUgVQtjg==,1738945459/videos/hls/58/bb/47/58bb471df0b2dda3998405fb35def112/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)