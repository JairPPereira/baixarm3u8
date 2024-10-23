import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/uEtJZ2MXv7PgRUYpipxy-A==,1729703780/videos/hls/66/b0/45/66b045ef25bb6ccb308112aa1a493ac7/hls-1080p-1416d.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)