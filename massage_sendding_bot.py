import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
import schedule


def send_massage(massage):    
    sckey = 'SCT86733TAFsMdy3BDAH0TqitL71y7VrW'
    title = "NOTICE"

    url = f"https://sctapi.ftqq.com/{sckey}.send?title={title}&desp={massage}"

    requests.get(url)
   
def f2pool_bot():
    # header={'upgrade-insecure-requests':'1',
	# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    # # browser = requests.get("https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395#ssssss",headers=header)
    # soup = BeautifulSoup(browser.text, "html.parser")#browser不能爬去动态网页
    # print(soup.prettify())  #輸出排版後的HTML內容
    # titles = soup.find_all("span", class_="value")
    # print(titles)


    # 设置options参数，以开发者模式运行
    option = ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_argument('--headless')
    browser = webdriver.Chrome(options=option)
    browser.get("https://www.f2pool.com/eth/0xab4bd79d7ee3a7b2e059294c39e60998e69bb395")
    # text = browser.page_source #获得网页源代码
    # print(text) #打印出源代码
    # is_online = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div/section[1]/div/section/div[3]/div/div[2]/span')
    # is_online = browser.find_element_by_class_name('item-val')
    global is_online
    is_online = browser.find_element_by_css_selector('#workers > div > div.content-container > div.worker-grid-header > div > ul > li:nth-child(2) > a > span')
    
    global f2pool_status
    f2pool_status = int(is_online.text)
    browser.quit()
    
def main_app():
    while True:
        f2pool_bot()
        if f2pool_status == 1:
            print("minner is running")
        else:
            print("massage sendding")
            try:
                send_massage("WARRING! minner is out work!")
            except:
                pass
        break

if __name__ == "__main__" :
    schedule.every(10).minutes.do(main_app)
    # schedule.every(3).seconds.do(main_app)
    while True:
        schedule.run_pending()
        # time.sleep(1)