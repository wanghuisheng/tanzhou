#  -*- coding:utf-8 -*-
from random import Random

from django.core.mail import send_mail

from users.models import EmailVerify
from tanzhou.settings import EMAIL_FROM


# 得到一个随机字符串
def random_str(randomlenght=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlNnMmOoPpQqRrSsTtUuVvWwXxYyZz012346789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlenght):
        str += chars[random.randint(0, length)]
    return str


# 发送邮件
def send_register_email(email, send_type="register"):

    # 实例化Email model.
    email_record = EmailVerify()

    code = random_str(16)

    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()


    # 设置邮箱的发送信息
    email_title = ""
    email_body = ""

    if send_type == "register":

        email_title = u"在线注册激活链接"
        email_body = u"请点击下面的链接激活你的账号：http://192.168.83.128:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])

        if send_status:
            pass
