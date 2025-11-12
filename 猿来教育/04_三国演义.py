# https://www.shicimingju.com/book/sanguoyanyi.html
import requests
from lxml import etree
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
response=requests.get(url,headers=header)
response.encoding='utf-8'
# print(response.text)
html=etree.HTML(response.text)
# items=html.xpath('//div[@class="book-mulu"]/ul/li/a')
items=html.xpath('//div[@class="list"]/a[@class="tabli"]/@href')
for item in items[:2]:
    # print('https://www.shicimingju.com/'+item)
    response=requests.get('https://www.shicimingju.com/'+item,headers=header)
    response.encoding='utf-8'
    # print(response.text)
    html=etree.HTML(response.text)
    detail=html.xpath('//div[contains(@class,"text") and contains(@class,"p_pad")]/p/text()')
    print(detail)