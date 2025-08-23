import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h.phncdn.com/hls/c6251/videos/202508/09/18751205/720P_4000K_18751205.mp4/index-v1-a1.m3u8?validfrom=1755978373&validto=1755985573&ipa=1&hdl=-1&hash=mhZkrYJqA1G2q4uKih3YJirv5%2Bo%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)