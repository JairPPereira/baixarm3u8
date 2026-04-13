import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://hls-cdn77.xvideos-cdn.com/DXRTWYP54qupxu_qMB8GjA==,1776092555/02153a27-e80c-4798-b9a9-dc7e4e3084f4/3/hls.m3u8'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)