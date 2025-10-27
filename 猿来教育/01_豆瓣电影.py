# https://movie.douban.com/review/best/
import requests
from lxml import etree

url='https://movie.douban.com/review/best/'
header={
    "authority": "movie.douban.com",
    "method": "GET",
    "path": "/review/best/",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "bid=X9geQKu_G-g; _pk_id.100001.4cf6=675402d1f3083c00.1760532914.; __utmz=30149280.1760532914.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmz=223695111.1760532914.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=ElZ3Nh6TNpHaYSSKYCQIhrMSVMPcbev9; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.1423551485.1760532914.1762854780.1762866829.4; __utmb=30149280.0.10.1762866829; __utmc=30149280; __utma=223695111.1616008295.1760532914.1762854780.1762866829.4; __utmb=223695111.0.10.1762866829; __utmc=223695111",
    "priority": "u=0, i",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "cross-site",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
response=requests.get(url,headers=header)
response.encoding = 'utf-8'
# print(response.text)
item=etree.HTML(response.text)
detail_list=item.xpath('//div[@class="review-list chart "]/div/@data-cid')
for detail in detail_list:
    detail_url = f"https://movie.douban.com/j/review/{detail}/full"
    response = requests.get(url=detail_url, headers=header)
    response.encoding = 'utf-8'
    print(response.json()['html'])
    break