import bs4 
import requests
url = 'https://pfaf.org/user/DatabaseSearhResult.aspx'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
print(soup)
