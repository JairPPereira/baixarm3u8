import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h-ph.rdtcdn.com/hls/videos/202309/20/439801141/720P_4000K_439801141.mp4/master.m3u8?validfrom=1739451059&validto=1739458259&hdl=-1&hash=Gnv7IuvsGOsY2I2aC8Qhy%2BoP9Uw%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)