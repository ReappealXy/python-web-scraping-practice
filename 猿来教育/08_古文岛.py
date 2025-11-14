# https://www.guwendao.net/
import requests
from lxml import etree
import re
url = 'https://www.guwendao.net/'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}
response=requests.get(url,headers=header)
response.encoding='utf-8'
# print(response.text)
html=etree.HTML(response.text)
details=html.xpath('//div[@class="sons"]/div[@class="cont"]')
# titles=html.xpath('//div[@class="sons"]/div[@class="cont"]//p[1]//b/text()')
# names=html.xpath('//div[@class="sons"]/div[@class="cont"]//p[2]//a/text()')
# content=html.xpath('//div[@class="sons"]/div[@class="cont"]//p/text()')
# print(titles,names,content)
for detail in details:
    title = ''.join(detail.xpath('.//p[1]//b/text()'))
    name = ''.join(detail.xpath('.//p[2]//a/text()'))
    content = ''.join(detail.xpath('.//div[contains(@class,"contson")]//text()'))
    print(title,name,content)