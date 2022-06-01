from selenium import webdriver

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get('https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395')


# import requests
#
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers={'User-Agent':user_agent}
# r = requests.get('https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395',headers=headers)
# print(r.content)
'''----------------------------------------'''
# import requests
# def getHTMLText(url):
#     try:
#         r=requests.get(url,timeout=30)
#         r.raise_for_status()
#         r.encoding=r.apparent_encoding
#         return r.text
#     except:
#         return "产生异常"
# if __name__ =="__main__":
#     url="https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395"
#     print(getHTMLText(url))
'''---------------------'''
# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get('https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395')
# r.status_code
# soup = BeautifulSoup(r.text,'html.parser')
# # print(soup,r.status_code)