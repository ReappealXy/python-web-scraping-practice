import requests
from lxml import etree
# /html/body/main/div[2]/div
url='https://spiderbuf.cn/web-scraping-practice/scraping-images-from-web'
base_url="https://spiderbuf.cn"
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
tree=etree.HTML(requests.get(url,headers=header).text)
res=tree.xpath('/html/body/main/div[2]/div/div')
count=1
for i in res:
    img_url=base_url+i.xpath('./img/@src')[0]
    img_name=i.xpath('./img/@alt')[0]
    # print(img_url,img_name)
    img_data=requests.get(img_url,headers=header).content
    with open(f'./imgs/{count}_{img_name}.jpg','wb') as f:
        f.write(img_data)
    print(f"{count}_{img_name}下载完成")
    count+=1