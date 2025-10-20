import requests
from lxml import etree

url='https://spiderbuf.cn/web-scraping-practice/scraper-login-username-password/login'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
data={
    "username":"admin",
    "password":"123456"
}
response=requests.post(url=url,headers=header,data=data)
response.encoding = 'utf-8'
# print(response.text)
tree=etree.HTML(response.text)
tr_list=tree.xpath('/html/body/main/div[2]/table/thead/tr/th/text()')
td_list=tree.xpath('/html/body/main/div[2]/table/tbody/tr')
for td in td_list:
    td_text=td.xpath('./td/text()')
    for th in range(len(tr_list)):
        header=tr_list[th]
        datas=td_text[th]
        print(f"{header}:{datas}")
    print('============================================')