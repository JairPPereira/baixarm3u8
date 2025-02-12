import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://gcore-vid.xvideos-cdn.com/FAxGGFDkYwO0bg20osrYmQ==,1739379942/videos/hls/5d/bb/c3/5dbbc3f023065426814669c2192ff1aa/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)