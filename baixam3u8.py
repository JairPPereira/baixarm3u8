import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://kv-h.phncdn.com/hls/videos/202406/20/454104701/720P_4000K_454104701.mp4/master.m3u8?hdnea=st=1750964164~exp=1750967764~hdl=-1~hmac=ee06f2565e14e08e679a9c4c8a1e1e83a5081f79'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)