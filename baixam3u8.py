import m3u8_To_MP4

if __name__ == '__main__':
    # URL do arquivo M3U8
    m3u8_url = 'https://edge2-waw-sprintcdn.r66nv9ed.com/hls2/01/03006/4zoyy2i2gjfd_o/master.m3u8?t=oHDngu3_dUciYqTTQTacBHtBX_-Rs4Gy5CD4cnhd94Q&s=1779742398&e=10800&f=53514570&srv=1075&asn=265175&sp=4000&p=0'
    
    # Baixar vídeo usando múltiplas threads
    m3u8_To_MP4.multithread_download(m3u8_url)

    # Ou, se você preferir usar a abordagem assíncrona:
    # m3u8_To_MP4.async_download(m3u8_url)