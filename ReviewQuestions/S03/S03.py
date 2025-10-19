import requests
from lxml import etree
url='https://spiderbuf.cn/web-scraping-practice/lxml-xpath-advanced'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
tree=etree.HTML(requests.get( url,headers=header).text)
res=tree.xpath('/html/body/main/div[2]/table')
headers=tree.xpath('/html/body/main/div[2]/table/thead/tr/th/text()')
tr_list = tree.xpath('/html/body/main/div[2]/table/tbody/tr')
datas_list=[]
for tr in tr_list:
    td_elements = tr.xpath('./td')
    row_data = [td.xpath('string(.)').strip() for td in td_elements]
    for i in range(len(headers)):
        header=headers[i]
        data=row_data[i]
        with open('S03.txt', 'a', encoding='utf-8') as f:
            f.write(f"{header}:{data}")
            f.write('\n')
    with open('S03.txt', 'a', encoding='utf-8') as f:
        f.write('=====================')
        f.write('\n')
