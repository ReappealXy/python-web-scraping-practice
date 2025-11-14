# https://www.mingchaonaxieshier.com/
import requests
from lxml import etree
url = 'https://www.mingchaonaxieshier.com/'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}
response=requests.get(url,headers=header)
response.encoding='utf-8'
html=etree.HTML(response.text)
title_head=html.xpath('//h2/a/text()')
title=html.xpath('//td/a/text()')
content_urls=html.xpath('//td/a/@href')
# print(content_urls)
# print(title_head, title)
for i in range(len(title_head)):
    print(title_head[i])
    for j in range(len(title)):
        print(title[j])
        chapter_url = content_urls[j]
        response=requests.get(url=chapter_url,headers=header)
        response.encoding='utf-8'
        html=etree.HTML(response.text)
        content=html.xpath('//div[@class="content"]//p/text()')
        story=[]
        for line in content:
            line=line.strip()
            if not line:
                break
            if "下一章：" in line or "上一章：" in line:
                break
            story.append(line)
            if "当年明月" in line:
                break
        print("".join( story))
        break
    break

    # content_header={
    #     "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    #                    "AppleWebKit/537.36 (KHTML, like Gecko) "
    #                    "Chrome/120.0.0.0 Safari/537.36"),
    #     "Referer":"https://www.mingchaonaxieshier.com/"
    # }
