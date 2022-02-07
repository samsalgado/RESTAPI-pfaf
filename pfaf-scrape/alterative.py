#Alterative API
import requests
import json
response = requests.get(
    'https://pfaf.org/user/Search_Use.aspx?glossary=Alterative'
)
print(response.json())
