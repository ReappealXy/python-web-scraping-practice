# https://www.pearvideo.com/
import requests
from lxml import etree
import re
url = 'https://www.pearvideo.com/'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer":"https://www.pearvideo.com/"
}

response=requests.get(url,headers=header)
response.encoding='utf-8'
html=etree.HTML(response.text)
video_hrefs = html.xpath('//div[@class="vervideo-tbd"]/a/@href')
for href in video_hrefs:
    video_header = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36"),
        "Referer": f"https://www.pearvideo.com/{href}",
    }
    contId = re.search(r'(?<=video_)\d+', href).group()
    video_url = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=114514'
    response = requests.get(video_url, headers=video_header)
    data = response.json()
    system_time = data['systemTime']
    src_url = data['videoInfo']['videos']['srcUrl']
    # print(src_url)
    real_url = src_url.replace(system_time, f"cont-{contId}")
    # print(contId)
    # print(real_url)
    response = requests.get(real_url, headers=video_header)
    with open(f'video/09_梨视频/{contId}.mp4', 'wb') as f:
        f.write(response.content)
        print(f'{contId}.mp4下载完成')
        break
