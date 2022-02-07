import requests
import json
response = requests.get(
    'https://pfaf.org/user/DatabaseSearhResult.aspx'
)
print(response.json())
response1 = requests.get(
    'https://pfaf.org/user/MedicinalUses.aspx'
)
print(response1)
