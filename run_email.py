# Solar
# handsome
# 发送邮件
from CRM_Page_Object.Run.runs import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def email (new):
    sever = 'smtp.qq.com'  # qq邮箱服务器
    port = 465  # 端口
    us = '1054989422@qq.com'    # 登录邮箱账号（发送者账号）
    pw = 'rxnvcvqfulwebcgh'     # 邮箱验证码
    rev = '1054989422@qq.com'    # 收件人

    # 编辑邮箱内容
    file = open (new,'rb')
    content = file.read ()
    file.close ()

    # 设置收发件人
    massage = MIMEMultipart ()
    massage ['from'] = us   # 设置发件人
    massage ['to'] = rev    # 设置接收人
    massage ['subject'] = 'CRM新增员工测试报告'     # 设置主题

    # 正文，用html格式
    body = MIMEText (content,'html','utf-8')
    massage.attach (body)   # 先挂起，避免先发送了

    # 附件，用base64格式
    fu = MIMEText (content,'base64','utf-8')
    fu ['Content-Type'] = 'application/octet-stream'    # 声明类型
    # 固定写法，定义附件名称
    fu ['Content-Disposition'] = 'attachment; filename = "CRM_add_test.html"'
    massage.attach (fu)     # 再次挂起，等会一起发送

    # 开始发送邮件
    smtp = smtplib.SMTP_SSL (sever,port)    # 先连接，传入服务器地址和端口号
    smtp.login (us,pw)      # 登录
    smtp.sendmail (us,rev,massage.as_string ())        # 发送邮件，as_string以字符串方式发送
    smtp.quit ()        # 关闭连接

wenjianku = os.listdir (lujing2)
lujing5 = lujing2 + wenjianku [-1]
email (lujing5)