# smtplib 用于邮件的发信动作
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
import os


import uiautomator2 as u2

device = u2.connect("10.125.56.167:5566")

str = "https://allapp.allapp.link/t/86rjW7986zLV/?v=m"
os.system("adb shell am start -a android.intent.action.VIEW -d"+str)

#os.system("adb shell screencap  /sdcard/screen.png")

#os.system("adb shell /sdcard/screen.png  /Users/app/PycharmProjects/testandroid/image/screen.png")



# 用于构建邮件头

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '836769422@qq.com'
password = 'nnxxlenjlydmbdbi'

# 收信方邮箱
to_addr = 'zhengjiafeng68@163.com'

# 发信服务器
smtp_server = 'smtp.qq.com'


# 邮件内容设置
content = MIMEText("<html><h2>test_image....</h2>", _subtype="html", _charset="utf-8")
msg = MIMEMultipart('related')
msg.attach(content)

# 添加图片附件
imageFile = r"./image/screen.png"
imageApart = MIMEImage(open(imageFile, 'rb').read(),imageFile.split('.')[-1])

imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
msg.attach(imageApart)

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
#msg = MIMEText('show_image', 'plain', 'utf-8')

os.remove("./image/screen.png")

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('test_url')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()