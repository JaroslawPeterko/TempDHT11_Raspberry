import sys
import Adafruit_DHT
import smtplib
temperatura_max = 24.0
fromaddr='mail1@gmail.com'
toaddrs='mail@gmail.com'
msg='Alarm - Temperatura w serwerowni osiągnela poziom krytyczny'
username='mail1@gmail.com'
password='Password'
humidity, temperatura = Adafruit_DHT.read_retry(11, 17)
if temperatura > temperatura_max:
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    msg='Alarm - Wzrost temperatury w serwerowni' + str(temperatura) + ' wilgotnosc' + str(humidity)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()        

else:
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    msg='OK temperatura w serwerowni' + str(temperatura) + ' wilgotnosc' + str(humidity)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
