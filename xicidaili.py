import requests
from bs4 import BeautifulSoup

for page in range(1,5):
    IPurl = 'http://www.xicidaili.com/nn/%s' %page
    rIP=requests.get(IPurl,headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6,ja;q=0.5,ko;q=0.4"
})
    IPContent=rIP.text
    soupIP = BeautifulSoup(IPContent,"html5lib")
    trs = soupIP.find_all('tr')

    for tr in trs[1:]:
        tds = tr.find_all('td')
        ip = tds[1].text.strip()
        port = tds[2].text.strip()
        protocol = tds[5].text.strip()
        if protocol == 'HTTP':
            httpResult = 'http://' + ip + ':' + port
            print(httpResult)
        elif protocol =='HTTPS':
            httpsResult = 'https://' + ip + ':' + port
            print(httpsResult)
