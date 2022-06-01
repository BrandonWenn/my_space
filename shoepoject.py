import requests
import smtplib
import schedule
import time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header
import json
'''基本配置'''
account ='1656830314@qq.com'#**这里填发件人邮箱，我用的是QQ邮箱**。
password = 'jevxxvdaqjmdfdcf'#**这里填发件人的授权码！不是登录密码！**
# receiver ='shoeshineboy@163.com'#**这里填收件人的邮箱。**
# receiver_1 = '770061896@qq.com'
'''功能'''
def sentence():
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content,note
def weather_spider():
    headers={
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    url='http://www.weather.com.cn/weather1d/101270102.shtml'#填写天气网站所在地的网址
    res=requests.get(url=url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    clothes1=soup.find(class_='li3 hot').find('p')
    clear = soup.find(class_="livezs").find('p')
    weather=weather1.text
    clothes=clothes1.text
    return tem,weather,clothes,clear
'''发邮件'''
def send_email(tem,weather,clothes,content,note):
    mailhost = 'smtp.qq.com'##把qq邮箱的服务器地址赋值到变量mailhost上，地址应为字符串格式
    qqmail = smtplib.SMTP_SSL(mailhost)##实例化并连接SMTP端口号。
    qqmail.connect(mailhost,465)#**如果放在阿里云服务器运行，只能465端口，25端口会被当做垃圾邮件。**
    qqmail.login(account,password)
    subject = 'SHOE\'s Robot '  # ***这里写邮件的标题***
    content= 'Hello!\n今日天气: '+tem+','+weather+',\n'+clothes+'\n'+content+'\n'+note
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    s = content + "\nOh wait a minite，您已欠下400万元巨款，且以日化 0.06% 的利息结算。\n今日金额为：" + balance() + "万元"
    message_1 = MIMEText(s, 'plain', 'utf-8')
    message_1['From'] = Header("最爱你的父亲", 'utf-8')
    message_1['To'] = Header("椿儿子", 'utf-8')
    message_1['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        qqmail.sendmail(account, receiver_1,message_1.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

'''执行'''
def job():
    print('开始一次任务')
    money()
    content,note=sentence()
    tem,weather,clothes= weather_spider()
    send_email(tem,weather,clothes,content,note)
    print('任务完成')
schedule.every().day.at("06:00").do(job)#定时七点执行任务。
while True:
    schedule.run_pending()
    time.sleep(1)#检查部署的情况，如果任务准备就绪，就开始执行任务。