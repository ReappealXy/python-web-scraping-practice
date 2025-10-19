# /html/body/table
import requests
from lxml import etree


url='https://spiderbuf.cn/web-scraping-practice/inner'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
tree=etree.HTML(requests.get(url,headers=header).text)
table_headers=tree.xpath('/html/body/table/thead/tr/th/text()')
tr_list = tree.xpath('/html/body/table/tbody/tr')
for tr in tr_list:
    td_elements=tr.xpath('./td')
    row_data=[td.xpath('string(.)').strip() for td in td_elements]
    for i in range(len(table_headers)):
        single_header=table_headers[i]
        data=row_data[i]
        with open('S06.txt', 'a', encoding='utf-8') as f:
            f.write(f"{single_header}:{data}")
            f.write('\n')
    with open('S06.txt', 'a', encoding='utf-8') as f:
        f.write('=====================')
        f.write('\n')