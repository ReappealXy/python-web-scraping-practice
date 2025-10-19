import requests
from lxml import etree
url='https://spiderbuf.cn/web-scraping-practice/web-pagination-scraper?pageno={}'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
datas_list=[]
for page in range(1,6):
    with open('S04.txt', 'a', encoding='utf-8') as f:
        f.write(f'第{page}页信息：')
        f.write('\n')
    current_url=url.format(page)
    tree = etree.HTML(requests.get(current_url, headers=header).text)
    res = tree.xpath('/html/body/main/div[2]/table')
    table_headers = tree.xpath('/html/body/main/div[2]/table/thead/tr/th/text()')
    tr_list = tree.xpath('/html/body/main/div[2]/table/tbody/tr')
    print(f"--- 开始爬取第 {page} 页: {current_url} ---")
    for tr in tr_list:
        td_elements = tr.xpath('./td')
        row_data = [td.xpath('string(.)').strip() for td in td_elements]
        for i in range(len(table_headers)):
            single_header=table_headers[i]
            data=row_data[i]
            with open('S04.txt', 'a', encoding='utf-8') as f:
                f.write(f"{single_header}:{data}")
                f.write('\n')
        with open('S04.txt', 'a', encoding='utf-8') as f:
            f.write('=====================')
            f.write('\n')
