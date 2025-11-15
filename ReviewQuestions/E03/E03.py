# url='https://spiderbuf.cn/web-scraping-practice/scraping-random-pagination'

import requests
from lxml import etree

url = 'https://spiderbuf.cn/web-scraping-practice/scraping-random-pagination'
header = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
response = requests.get(url, headers=header)
# print(response.text)
tree = etree.HTML(response.text)
href_list = tree.xpath('//ul[@class="pagination"]/li/a/@href')
for hrefs in href_list:
    print("https://spiderbuf.cn" + hrefs)
