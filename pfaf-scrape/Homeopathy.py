from urllib import response
import requests
import json
response = requests.get(
    'https://pfaf.org/user/Search_Use.aspx?glossary=Homeopathy'
)
print(response.json())
