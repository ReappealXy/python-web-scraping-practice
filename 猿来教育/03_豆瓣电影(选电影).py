import requests

url = 'https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie'

headers = {
    "Referer": "https://m.douban.com/movie/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}
start=0
all_itemts=20
while True:
    params = {
        "start": start,
        "limit": all_itemts
    }
    response = requests.get(url, headers=headers, params=params)
    response.encoding = 'utf-8'
    data=response.json()
    for item in data.get("items",[]):
        print(item.get("title"))
    start+=20
    if start>=data.get("total",0):
        break