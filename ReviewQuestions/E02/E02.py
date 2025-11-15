import requests
from lxml import etree

url = 'https://spiderbuf.cn/web-scraping-practice/web-scraping-with-captcha/list'

# 注意：要把Cookie改成自己的
myheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
             'Cookie':'admin=abf0805f1e529daef29e7d9d471d6d75'}

payload = {'username':'admin','password':'123456'}

html = requests.get(url, headers=myheaders, data=payload).text
print(html)