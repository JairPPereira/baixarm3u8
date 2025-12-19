import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://cdn77-vid.xvideos-cdn.com/0MYgkWBm48iU_aLs8WsDKQ==,1766151025/videos/hls/74/14/1d/74141d73a2ebaebbee7aa14b0998eb0e/hls-480p-23718.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)