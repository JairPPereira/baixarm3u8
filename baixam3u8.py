import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://video-cf.xhcdn.com/akFnLUI5yLFUkKwbiFncuRM3atmt%2FUvkZ2HK9gH%2BDMU%3D/87/1739466000/media=hls4/multi=256x144:144p:,426x240:240p:,854x480:480p:,1280x720:720p:/021/632/085/_TPL_.av1.mp4.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)