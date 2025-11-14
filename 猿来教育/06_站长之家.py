# https://sc.chinaz.com/tupian/renwutupian.html
import requests
from lxml import etree
url = 'https://sc.chinaz.com/tupian/renwutupian.html'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}
img_header={
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Referer":"https://sc.chinaz.com/tupian/renwutupian.html"
}
response=requests.get(url,headers=header)
response.encoding='utf-8'
# print(response.text)
html=etree.HTML(response.text)
img_urls=html.xpath('//div[@class="item"]/div/a/@href')
for img_url in img_urls:
    # print('https://sc.chinaz.com'+img_url)
    url='https://sc.chinaz.com'+img_url
    response=requests.get(url,headers=header)
    response.encoding='utf-8'
    html=etree.HTML(response.text)
    img_name=html.xpath('//div[@class="img-box"]/img/@alt')[0]
    img_src=html.xpath('//div[@class="img-box"]/img/@src')[0]
    img_src='https:'+img_src
    # print(img_name,img_src)
    response_img=requests.get(url=img_src,headers=img_header)
    with open(f'img/06_站长之家/{img_name}.jpg', 'wb') as f:
        f.write(response_img.content)

    break