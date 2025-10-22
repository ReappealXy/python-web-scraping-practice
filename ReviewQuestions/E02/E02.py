import requests
from lxml import etree

url='https://spiderbuf.cn/web-scraping-practice/web-scraping-with-captcha/list'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'Cookie':'admin=23656d1a8d6c426eb3069f41662e74de'
}
response=requests.get(url=url,headers=header)
response.encoding = 'utf-8'
print(response.text)
# tree=etree.HTML(response.text)
# tr_list=tree.xpath('/html/body/main/div[2]/div/div/table/thead/tr')
# # print(tr_list)
# for i in tr_list:
#     tr_text=i.xpath('./th/text()')
#     print(tr_text)
