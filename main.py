import requests
from bs4 import BeautifulSoup
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os
import lxml

load_dotenv()

#You can get these headers from http://myhttpheader.com/
headers = {
    "Accept-Language" : os.getenv("Accept-Language"),
    "User-Agent" : os.getenv("User-Agent") 
}

PRODUCT_URL = "https://www.amazon.com/Oculus-Quest-Carrying-Lightweight-Portable-Protection/dp/B08F5VCNCY/ref=sr_1_10?crid=2PLAANILQ405B&keywords=Oculus&qid=1640425752&sprefix=oculus%2Caps%2C188&sr=8-10"
email = os.getenv("target_email")
notification_price = 50


response = requests.get(PRODUCT_URL,headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price = soup.find(name="span", class_="a-offscreen")
price = float(price.getText().split("$")[1])

if notification_price > price:
    notification = NotificationManager(price,notification_price,PRODUCT_URL,email)
    notification.send_email()
