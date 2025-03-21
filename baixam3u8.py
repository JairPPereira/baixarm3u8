import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xnxx-cdn.com/jbXelfJLEhrejwRsxItN_Q==,1742569272/videos/hls/49/d9/92/49d992ab3e1fcaf9d9bd84b7983a93ff/hls-1080p-28168.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)