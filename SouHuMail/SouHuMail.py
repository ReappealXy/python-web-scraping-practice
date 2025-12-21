import execjs
import json
import requests

with open('SouHuMail.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
ctx = execjs.compile(js_code)
url = 'https://v4.passport.sohu.com/i/login/101305'
password='linxingyu1025'
pwd = ctx.call('md5', password)
data={
    "userid": "19523639689@sohu.com",
    "password": pwd,
    "appid": "101305",
    "nf": "1"
}
headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9',
    'Cookie': 'a=123; reqtype=pc; gidinf=x099980109ee1bcb04a0d4413000625ab01893559944; _dfp=kS/trnFjiFFZIsRc1Fyzl/Xg3ot3MI7m2uSSU4CtIkU=; t=1766323851317; jv=a9732bf40b45ecc480f090d27c03d74c-G66iLqCW1766324021637',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'origin': 'https://mail.sohu.com',
    'referer': 'https://mail.sohu.com/',
}
response = requests.post(url, data=data, headers=headers)
print(response.text)