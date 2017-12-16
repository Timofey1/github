# This Python file uses the following encoding: utf-8

import os
from bottle import *
import requests
#import json
#from bs4 import BeautifulSoup

@route('/sms')
def sms():
    return '''
<!DOCTYPE html>
 <html>
  <head>
  <meta charset="utf-8">
  <title>Телефон</title>
 </head>
 <body>
  <form method="POST" action="/sms">
   <p>Ваше сообщение: <input name="message"></p>
   <p>Телефон в формате 7хххххххххх:  <input type="tel" name="tel" 
   pattern="7[0-9]{10}"></p>
   <p><input type="submit" value="Отправить"></p>
  </form>
 </body>
</html>
'''

@route('/sms', method="POST")
def send_sms():
    message = request.forms.get("message")
    phone = request.forms.get("tel")

    login = "horoomy"
    psw = "b09782d94fa57631762f36b991c5380a"
    
	class SMS:
        def __init__(self, l, p):
            self.login = l
            self.psw = p
            self.url = "http://smsc.ru/"

        def doRequest(self, rqData, url):
            rqData["login"] = self.login
            rqData["psw"] = self.psw
            r = requests.get(self.url + url, params=rqData)
            return r.text

        def sendSMS(self, phone, message):
            rqData = {"phones": phone, "mes": message}
            return self.doRequest(rqData, "sys/send.php")

    sms = SMS(login, psw)
    sms.sendSMS(phone,message)
    return "<p>Your message has been sent.</p>"

run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
