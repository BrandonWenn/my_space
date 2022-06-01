import requests
# from lxml import html

url = 'https://p2p.binance.com/zh-CN/express/buy/USDT/CNY'
URL = 'https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395'
proxies = {'http': 'http://localhost:7890', 'https': 'http://localhost:7890'}
html = requests.post(URL, proxies=proxies, verify=False) #verify是否验证服务器的SSL证书
# print(html.text)

response = html.text

def xpath_for_parse(response):
    books = response.xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/span[2]")
    print(books)
    # for book in books:
    #     title = book.xpath('div[@class="name"]/a/@title')[0]
    #     print(title)

if __name__ == '__main__':
    xpath_for_parse(response)


