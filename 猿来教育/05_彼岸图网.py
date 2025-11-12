# https://pic.netbian.com/
import requests
from lxml import etree
url = 'https://pic.netbian.com/'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
response=requests.get(url,headers=header)
response.encoding='gbk'
# print(response.text)
html=etree.HTML(response.text)
items=html.xpath('//div[@class="slist"]/ul/li/a/span/img/@src')
# print( items)
for item in items:
    print('https://pic.netbian.com/'+item)