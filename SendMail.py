# -*- coding: utf-8 -*-
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Weather import *
# from Iciba import get_iciba_everyday_chicken_soup
mail = MIMEMultipart() 
# 发送邮件服务器
smtpserver = 'smtp.sina.cn'
# 发送邮箱用户名和密码
user = 'xxxx@sina.com'
password = 'xxxx'
# 收件人，多个收件人用逗号隔开
username_recv = 'xxxx,xxxx'
# 邮件正文内容

mail.attach(MIMEText(str(get_weather())))
mail['From'] = Header(user)
mail['To'] = Header(username_recv)
subject = "乌鲁木齐新市区近7天天气预报"
mail['Subject'] = Header(subject) 
smtp = smtplib.SMTP()
smtp.connect(smtpserver, 25)
smtp.login(user, password)
smtp.sendmail(user, username_recv.split(','), mail.as_string())
smtp.quit()
