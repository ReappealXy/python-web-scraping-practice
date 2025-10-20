import requests
import json

url='https://spiderbuf.cn/web-scraping-practice/iplist'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
response=requests.get(url,headers=header)
response.encoding = 'utf-8'
res=response.text
# print(res)
# print(type(res))
# print(res)
# print(type(res))

res=json.loads(res)

for item in res:
    print(
        f"IP地址：{item['ip']}\n"
        f"MAC地址：{item['mac']}\n"
        f"设备名称：{item['name']}\n"
        f"设备类型：{item['type']}\n"
        f"操作系统：{item['manufacturer']}\n"
        f"开放端口：{item['ports']}\n"
        f"在线状态：{item['status']}"
    )
    print('=========================================')
