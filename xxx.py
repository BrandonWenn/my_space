import requests
from bs4 import BeautifulSoup
import schedule
import time
import re
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

account ='1656830314@qq.com'
password = 'jevxxvdaqjmdfdcf'
# receiver ='2199564347@qq.com'
receiver ='shoeshineboy@163.com'
def senten():
    headers = {
        'origin': 'https://y.qq.com',
        'referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    url = 'https://www.banbaowang.com/haojuzi/166349/'  # 填写天气网站所在地的网址
    res = requests.get(url=url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    x1 = str(soup)
    x = re.findall("(?<=<p>)[\s\S]*?(?=</p>)", x1)
    num = random.randint(1, 29)
    senten_get=x[num]
    return senten_get

def send_email(senten_get):
    mailhost = 'smtp.qq.com'##把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP_SSL(mailhost)##实例化并连接SMTP端口号。
    qqmail.connect(mailhost,465)#**如果放在阿里云服务器运行，只能465端口，25端口会被当做垃圾邮件。**
    qqmail.login(account,password)
    subject = '孙袜子教育之路'
    s = senten_get
    message= MIMEText(s, 'plain', 'utf-8')
    message['From'] = Header("最爱你的爷爷", 'utf-8')
    message['To'] = Header("孙儿子", 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    senten_get = senten()
    send_email(senten_get)
    print('任务完成')
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)






