import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h.phncdn.com/hls/videos/202409/15/457801111/720P_4000K_457801111.mp4/master.m3u8?validfrom=1756373215&validto=1756380415&ipa=1&hdl=-1&hash=eftM3GVDmGV%2FILip%2Bley2xZNrOI%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)