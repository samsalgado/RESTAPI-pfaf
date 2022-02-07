#API Call   
from urllib import response
import requests
response = requests.get(
'https://pfaf.org/user/Search_Use.aspx?glossary=Aromatherapy'
)
print(response.json())
