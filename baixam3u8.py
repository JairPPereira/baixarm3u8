import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h.phncdn.com/hls/videos/202308/04/436805901/720P_4000K_436805901.mp4/master.m3u8?validfrom=1757323012&validto=1757330212&ipa=1&hdl=-1&hash=7ErVNc5GHGIhHqRE6ovrI%2ByyC24%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)