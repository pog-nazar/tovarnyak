from bs4 import BeautifulSoup
import requests

url = "https://lugi.com.ua/index.php?route=common/login_modal/login_validate"
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0"
}

data = {
    "emailpopup": "dise8600@gmail.com",
    "passwordpopup": "qwerty123456"
}

response = session.post(url, data=data, headers=headers).text

print(response)
