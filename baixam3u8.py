import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://gcore-vid.xnxx-cdn.com/Kz4mSW_sQ15GQ5Jp5Ll3Eg==,1741881588/videos/hls/92/05/93/920593331a4c6d6476028d8e612cb650/hls-1080p-38714.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)