#Building a Python App that Tracks the prices of face masks

#importing the libraries  
import requests
from bs4 import BeautifulSoup
import smtplib
import time 

URL='https://www.emag.ro/set-50-bucati-masti-faciale-de-unica-folosinta-nesterile-produs-vandut-fara-adaos-comercial-mastipc50/pd/D3DWMMMBM/?ref=others_also_viewed_control_1_1&provider=rec&recid=rec_43_b7f90bd2551731be030cc273de92a0281147d07ce32ed9b1b9008fe95de3c8d2_1590336058&scenario_ID=43'

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#first function,  for scraping the data 
def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title=soup.find(class_="page-title").get_text()
    price=soup.find(class_='product-new-price').get_text()
    converted_price=float(price[64:66])
 
    print(title.strip())
    print('Price :',converted_price,'LEI')
    
    if(converted_price < 60):
        send_mail()


#second function, for sending the information to ourself via email 

def send_mail():
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #here we put our conection 
    server.login('radu.zaharia@gmail.com','password')

    subject='Price fell down'
    body= 'Check the link https://www.emag.ro/set-50-bucati-masti-faciale-de-unica-folosinta-nesterile-produs-vandut-fara-adaos-comercial-mastipc50/pd/D3DWMMMBM/?ref=others_also_viewed_control_1_1&provider=rec&recid=rec_43_b7f90bd2551731be030cc273de92a0281147d07ce32ed9b1b9008fe95de3c8d2_1590336058&scenario_ID=43'

    msg=f"Subject: {subject}\n\n{body}"

    server.sendmail('radu.zaharia@gmail.com',
        'radu.zaharia@gmail.com',msg)
    print('email sent')

    server.quit()

#The amout of time (in seconds) which our app checks for the price every day
while(True):
    check_price()
    time.sleep(3600)
