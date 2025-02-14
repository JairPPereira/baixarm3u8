import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://ip396432093.ahcdn.com/key=2xirRnubvLIsWg5EUiMe+Q,s=,end=1739570400/data=206.84.35.17-dvp/state=Z6+NzlQj/reftag=078545589/media=hls4/ssd8/21/9/366673609.mp4/index.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)