from selenium import webdriver
from selenium.webdriver.common.by import By


# driver.maximize_window()

x = input('do you have set a VPN:（y/n）')
if x == "y":
    driver = webdriver.Chrome()
    driver.get('https://bulink.xyz/login/')
else:
    driver = webdriver.Chrome()
    driver.get('https://burstlinker.com/login/')

driver.find_element(By.NAME,'username').send_keys("1656830314@qq.com")
driver.find_element(By.XPATH,'//*[@id="id_password"]').send_keys("qwertyuiop")
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div/form/div/p[1]/button').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[4]/div/button').click()
