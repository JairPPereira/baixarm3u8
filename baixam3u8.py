import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h.phncdn.com/hls/c6251/videos/202508/06/18415975/720P_4000K_18415975.mp4/master.m3u8?validfrom=1756218183&validto=1756225383&ipa=1&hdl=-1&hash=BtfH6E1MxMQZsi0g3l9zDpbWn98%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)