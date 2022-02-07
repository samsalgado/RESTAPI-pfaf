from bs4 import BeautifulSoup
import bs4
import requests
url = 'https://pfaf.org/user/MedicinalUses.aspx'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
print(soup)

