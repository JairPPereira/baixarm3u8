import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://hls-cdn77.xvideos-cdn.com/zmbCgScIfpPWIcukjZTwpw==,1772031976/dd5cc71a-0d24-41e4-a351-846cc8ccfa2d/0/hls-720p.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)