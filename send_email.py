import smtplib
import os

PASSWORD = os.environ.get('yandex_pass')
USERNAME = os.environ.get('yandex_email')

def send_email(to_email,message):
    email = "articula93@yandex.ru"
    password = "wjphghaxrpyfppkk"
    # to_email = "testapiivan@yandex.ru"

    server = smtplib.SMTP_SSL('smtp.yandex.ru',465)
    server.ehlo()
    server.login(email,password)
    # message = "one,two,three"
    server.set_debuglevel(1)
    server.sendmail(email,to_email,message)
    server.quit()

    return True

# send_email(to_email = "testapiivan@yandex.ru",message="one,two,three")