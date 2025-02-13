import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ev-h.phncdn.com/hls/videos/202306/23/434112211/720P_4000K_434112211.mp4/master.m3u8?validfrom=1739450100&validto=1739457300&ipa=206.84.35.67&hdl=-1&hash=%2BnQYS%2Fk8EOE2bV6%2Fwq437xmbVWM%3D'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)