import smtplib
from dotenv import load_dotenv
import os


load_dotenv()

my_email = os.getenv("my_email")
password = os.getenv("password")

class NotificationManager:

    def __init__ (self,current_price,tracked_price,URL,email):
        self.current_price = current_price
        self.tracked_price = tracked_price
        self.URL = URL
        self.email = email

    def send_email(self):
        self.message = f"Subject:Low Price For Your Product!\n\nThe current price is {self.current_price}, lower than the price you set of {self.tracked_price}.\n\nBuy now! {self.URL}."
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email , password=password)
            connection.sendmail(from_addr=my_email, to_addrs=self.email, msg=self.message)
            connection.close()
            print("Email was sent!")
