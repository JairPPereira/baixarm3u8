import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/cWQ4KDxXNZhHHzAdSM1LPw==,1740760990/videos/hls/d1/07/4f/d1074fae53fdc9baa27907f6787843ad/hls-1080p-be32d.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)