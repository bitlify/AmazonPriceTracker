import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = # URL of amazon product

headers = {"User-Agent": #Your User Agent, google "My User Agent" to get it}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    price = soup.find(id="priceblock_ourprice").text
    converted_price = float(price[1:6])

    if (converted_price < #Price you want the item to drop to):
        send_mail()

    print(converted_price)

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587) #Use gmail for this
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(#your email, #make a new app password (need 2 steo verification for this to work))

    subject = "Price Fell Down!"
    body = "Check the amazon link: Link"

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        ""#email to send from, use your own,
        ""#email to send to, use your own,
        msg
    )

    print("EMAIL HAS BEEN SENT!")

    server.quit()

while(True):
    check_price()
    time.sleep(3600)# checks price every hour