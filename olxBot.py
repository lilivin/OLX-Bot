from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from lxml import etree
from bs4 import BeautifulSoup
import time

# Wpisz tutaj link
URL = 'https://www.olx.pl/nieruchomosci/mieszkania/warszawa/q-Mieszkanie-na-wynajem/?search%5Border%5D=created_at%3Adesc'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

current_id = ""

def check_price():
    global current_id  # Declare current_id as a global variable

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    dom = etree.HTML(str(soup))
    found_id = dom.xpath("/html/body/div[1]/div[2]/div[2]/form/div[5]/div/div[2]/div[6]/a")[0].attrib.get('href')
    if current_id != found_id:
        print("New id!")
        current_id = found_id
        if not found_id.startswith("https://"):
            found_id = "https://www.olx.pl" + found_id
        message = f"Nowe ogłoszenie {found_id}"
        #Wpisz tutaj telegram token
        TOKEN = ""
        #Wpisz tutaj telegram chat id token
        chat_id = ""
        chat_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(chat_url).json())

    print(current_id)


while True:
    check_price()
    time.sleep(60)