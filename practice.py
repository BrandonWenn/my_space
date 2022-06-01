import requests
from lxml import html

URL = 'https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395'

proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}
html = requests.post(URL, proxies=proxies, verify=False) #verify是否验证服务器的SSL证书
response = html.text
# print(response)

def xpath_for_parse(response):
    # selector = html.fromstring(response)
    x = response.xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/span[2]')
    print(x)

if __name__ == '__main__':
    xpath_for_parse(response)


