import requests
from lxml import etree

url='https://spiderbuf.cn/web-scraping-practice/requests-lxml-for-scraping-beginner'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
tree=etree.HTML(requests.get( url,headers=header).text)
res=tree.xpath('/html/body/main/div[2]/table')
headers=tree.xpath('/html/body/main/div[2]/table/thead/tr/th/text()')
tr_list = tree.xpath('/html/body/main/div[2]/table/tbody/tr')
datas_list=[]
for tr in tr_list:
    row_data = tr.xpath('./td/text()')
    if len(row_data) == len(headers):
        for i in range(len(headers)):
            header = headers[i]
            data = row_data[i]
            print(f"{header}: {data}")
    else:
        # 票不对，直接不让进，并发出警告
        print(f"!!! 警告: 发现一行数据不完整，已跳过。该行数据为: {row_data}")
    print('====================================')