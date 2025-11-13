# https://pic.netbian.com/
import requests
from lxml import etree
url = 'http://pic.netbian.com'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
header_img={
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Referer":"https://pic.netbian.com/"
}
response=requests.get(url,headers=header)
response.encoding='gbk'
# print(response.text)
html=etree.HTML(response.text)
href_items = html.xpath('//div[@class="slist"]/ul/li/a/@href')
for href in href_items:
    # print(url+ href)
    detail_url=url+href
    response=requests.get(url=url+href,headers=header)
    response.encoding='gbk'
    html=etree.HTML(response.text)
    img_name=html.xpath('//div[@class="photo-pic"]/a/img/@title')[0]
    img_src=html.xpath('//div[@class="photo-pic"]/a/img/@data-pic')[0]
    img_src=url+img_src
    print(img_name,img_src)
    response_img=requests.get(url=img_src,headers=header_img)
    with open(f'img/{img_name}.jpg', 'wb') as f:
        f.write(response_img.content)
    break