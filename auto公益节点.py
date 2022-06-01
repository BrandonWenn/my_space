from selenium import webdriver
from selenium.webdriver.common.by import By


# driver.maximize_window()

x = input('do you have set a VPN:（y/n）')
if x == "y":
    driver = webdriver.Chrome()
    driver.get('https://api.tianquege.top/#/login')
else:
    driver = webdriver.Chrome()
    driver.get('https://api.tianquege.top/#/login')

driver.find_element(By.XPATH,'//*[@id="main-container"]/div[2]/div/div/div[2]/div[1]/div/div/div[1]/input').send_keys("1656830314@qq.com")
driver.find_element(By.XPATH,'//*[@id="main-container"]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/input').send_keys("qwertyuiop")
driver.find_element(By.XPATH,'//*[@id="main-container"]/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button').click()
