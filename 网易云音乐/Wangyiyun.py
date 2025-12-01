import execjs
import json
import requests

# 1. 读取你的 js 文件
with open('index.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# 2. 编译 JS 环境
ctx = execjs.compile(js_code)
url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=43a69316397af57707ffc5ed03fe7f18'

data = {
    "csrf_token": "43a69316397af57707ffc5ed03fe7f18",
    "encodeType": "aac",
    "ids": "[1325905146]",
    "level": "standard"
}
# datas = json.dumps(data, separators=(',', ':'))
res = ctx.call('Rexy', data)
header= {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-length": "502",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "P_INFO=17379208953|1708490582|1|g10_client|00&99|null&null&null#gud&null#10#0|&0|null|17379208953; _ga=GA1.1.1261089578.1716200609; Qs_lvt_382223=1716362974%2C1716363755%2C1716364081%2C1716367959%2C1725453965; Qs_pv_382223=458633274273904400%2C3188201531400943600%2C4544120393276856000%2C1493063788265416000%2C1207181595421603000; _ga_C6TGHFPQ1H=GS1.1.1725453965.4.0.1725453965.0.0.0; _clck=4u5q8k%7C2%7Cfow%7C0%7C1601; NMTID=00OAkGE8wLq3FCSKkksoskqLLirVpsAAAGR1XQbag; _iuqxldmzr_=32; _ntes_nnid=2ecb02716624e09dc7311a24a408957c,1725863041370; _ntes_nuid=2ecb02716624e09dc7311a24a408957c; WEVNSM=1.0.0; WNMCID=mroxmm.1725863042196.01.0; WM_TID=%2FJW2DbFUQBVFVRRUARLBThlN4aWlHEXj; ntes_utid=tid._.%252FsJIL8E5YGRBRgEQVBeFxMxFYxUHzoC9._.0; sDeviceId=YD-d3HJ1xmCJwpEVlBFQAKAaTOAmroxpzYG; __snaker__id=HO8O8ZODOXnULdUq; Hm_lvt_f8682ef0d24236cab0e9148c7b64de8a=1725885448; vinfo_n_f_l_n3=dcf977109111685c.1.14.1687962991019.1726740183913.1730729590313; __root_domain_v=.163.com; _qddaz=QD.411457725312278; ntes_kaola_ad=1; WM_NI=vD6jiT2lS8sP0yUUtwViENXj410OUb8crr3JbRM9aRsz%2FoBlY5n2%2FnZuJrQAfAOGUHuHI%2B%2BdGZ5kg4caXqUwHsZbm9kQc1F4iusJn74Ojl1TqdHSow1cOUsyoxB6UuWSdnQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee99b15d829fbeb4d964b3ef8fa6c54b938b8fb0c644f3abf9a2ae74b0aefad8e92af0fea7c3b92ab69cfa8bec60f2b49dd9f25cf4a79bb6f77d96b78bafdb62f8ef00b0d86afcbdbe93b242a28e83dae45ab1a6e190c1689beba2d3ae669aab8693d44ba69f81a8d844b79887ccaa708586fb8ce640a1bf9892d87d8cad9683f033a98fadd2c540ababbdabed3df891a68db460b3bc88b4ee7df3bd81b6f273ada88ed7d87f958dac8fd437e2a3; gdxidpyhxdE=%2BPAj7HksGGzjJCxUfRUiHXIosYc%5CdEL%2FNGniQXxTaHwUKmp5l0bzgEkg6aaZDbtiZqTf9UK5v3BEMEedm31faEQJm7BBSlH%2Ff4m1PBtoMWEYLp1YX3%2F5vSw%2BkVjGhck91LNarSuEVM7k1ImlQl%5CwB%2Fdeu40vzKUWXeuaOKgr2zP%2F585M%3A1731932284106; __csrf=985eb2fde4e1bd422dcd8f3defbb5889; MUSIC_U=00DBC31BCF1CC0DA1D5EDF11E4F473A591F50F0423CB08B19E03C3823521913E74A3BF0A487F52CD24824BD2D7570841DBC13672546849B13D13754DC5528765921AA4DF73235EC1E7800C8781FB5F4E354321C87642328A2562787F5CA547A8FDC0C08D949C19523574132B7AE84D9A07B1B0E57B213BC04CC4EF23C9BF5FCB3B31E79C3CD215B73F7BFF18C179DF8B495857B2D5BE3A609799EF2D5074B07F448603A7686111EA5BB8A807015334EA805F946028D050DBF0BA5DF3DCA5738A3D72C51D7BEA5320F09DB1D67000EBB87BD82E82F8A780453C227EECA7D842249A2A4DFC6BBF5DC392AF2C4DBC375A71F71D3EBC9F2BE68EF71B9AC8952429762A8BA36D2FE5C5B2523D1AFA44166F399A3AE7B01C004249B5BFD6196DDC57A1860C7DDAE64159A79F69A31C4B9C518D82033B306153CA650D412C4D4535F504C0A779674F46E55A4B038B4FAA6E03C5155200956D315EFB79A089227529B92058; playerid=28552755; JSESSIONID-WYYY=ABp2rKfUuKOGKrx4E%5CmuYyE2OXqE3flwYKPgrhP9w7UynS2R%2F%5CqK5%2FjMow7u9uOkBSh6Ha0UpEnD%5C%2BeXjZm%5CW5xT5E2xRZ%2FmcEXTJjZB1ZkPOmJ9XvAP8jlJVCleJ2hU1RobfWHe4MkYthfjbTDiQcE39T%2Bitmnjlow5%2FXhBcNQVEg8b%3A1731934430306",
    "dnt": "1",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://music.163.com/",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
form={
    'params': res['encText'],
    'encSecKey': res['encSecKey']
}
# print(res)


response = requests.post(url, data=form, headers=header)
result=response.json()
print(result['data'][0]['url'])