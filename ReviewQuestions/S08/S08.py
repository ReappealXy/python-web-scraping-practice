import requests
from lxml import etree


url='https://spiderbuf.cn/web-scraping-practice/scraper-via-http-post'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
data={
    "level":"8"
}
response=requests.post(url,headers=header,data=data)
response.encoding = 'utf-8'
# print(response.text)
tree=etree.HTML(response.text)
th_list=tree.xpath('/html/body/main/div[2]/table/thead/tr/th/text()')
tr_list=tree.xpath('/html/body/main/div[2]/table/tbody/tr')
for tr in tr_list:
    td_elements=tr.xpath('./td')
    row_data=[td.xpath('string(.)').strip() for td in td_elements]
    for i in range(len(th_list)):
        header=th_list[i]
        data=row_data[i]
        print(f"{header}:{data}")
