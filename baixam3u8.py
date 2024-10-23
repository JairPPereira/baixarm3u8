import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h-ph.rdtcdn.com/hls/videos/202406/20/454104701/720P_4000K_454104701.mp4/index-v1-a1.m3u8?validfrom=1729693891&validto=1729701091&hdl=-1&hash=Uc0J4a210gtrGOS6bGgIoEnwBkw%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)