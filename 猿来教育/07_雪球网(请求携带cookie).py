# url='https://xueqiu.com/'
import requests
from lxml import etree
url='https://xueqiu.com/'
header={
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/120.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer":"https://xueqiu.com/",
    "Cookie":"cookiesu=621760258688616; device_id=5295cdcbf036a1d79127565885f28c6a; smidV2=20251012164449484e5738cd83beef1a5fd6b87eee60c300ab971c3d8266680; acw_tc=3ccdc16a17631853696911370e7deeef89f65fc65f1cc282d99a04de0de2f4; xq_a_token=089d79f06ee92d795d3698468670a5d9dbadf407; xqat=089d79f06ee92d795d3698468670a5d9dbadf407; xq_r_token=33c99b4c5478c77154f46091eb752528dea18955; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTc2NTUwMjE0MSwiY3RtIjoxNzYzMTg1MzU1NjY4LCJjaWQiOiJkOWQwbjRBWnVwIn0.cK4H5Y9z12DHmBZ6wMNMIclwWmgdiRNbVHyD7M5TXsYmQQ1dkIpJyNQTMk-tPxcQ2wxkUqQabOIbw11lymw7JkgugePWUGiwkHBfy8HJhsDiYGQU3aRq0MtkOIXlP2sAh-mkOFMZ4psmrjdRlRLEbdkfH1ESOKbBsY_u1e1bxWiYh6JJGJK9LEGYMjHvwMuKn0cr77jxrNIjDrhzESyRNirUbb2r8eu8deOKgEBDfFdjN_pshSdBQEQmFH1Q5syPteeheGUYQsgvf8EReYXA1Ah0x9PjZkE9yusbCAxXrSu0SKVXBGljiyHuM_CrXBDTRqtMlePfVJ6ybBA6_zgcNQ; u=621760258688616; Hm_lvt_1db88642e346389874251b5a1eded6e3=1763099532,1763185371; HMACCOUNT=AF6031E31D1EF5A6; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1763185785; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=f8Y+SYrUG0RpcQNJaYnhPaMkg5hgv5zaA4rqN2qSntydYhA2ti8A8u38K0r9d4/9w3LOGDKQBciAr1neL4hchw%3D%3D; ssxmod_itna=1-GqAhY57KBKYIxWqYj9gDYk1KD7DRC0xBP01DpxYK0CHDLxn_5GdoR=eH_=dD9ml0LR4YVnEqDs=GY4GzDiMPGhDBmAHeSAwy4tiW9YE5==nhG0rPvLC0TbtlB1mwlmIrvDbZqv5QY/lrYqGLDY=DCdxNnbeD483Dt4DIDAYDDxDWDYoqxGtTDG=D7ER=Zludxi3DbhWDmwiabpaD0Rm3sjaoDDtvYeG2WxTtDDNtQIq4Bhrz7PD_YjaTlpue8UhKfeDMWxGXGGktfWyUVIwrkUSLaZA5xB69xBjN61TspxubxaarlBj/POez7D_YN=B5q7NCYxlGD_GhzD4zhqdYx_GDNBKzGq=GhKoiDWeDD3it_rCrzY4yPXgr3qONrQ0HDKDrvD6qNjwzjPwjqsDehDxzjeY7xKUDYfADzDxD; ssxmod_itna2=1-GqAhY57KBKYIxWqYj9gDYk1KD7DRC0xBP01DpxYK0CHDLxn_5GdoR=eH_=dD9ml0LR4YVno4DW_KEWWurN=Uu5ihiBxhonv4D"
}
response=requests.get(url,headers=header)
print(response.text)