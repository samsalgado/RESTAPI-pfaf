import requests 
response = requests.get(
    'https://pfaf.org/user/PlantUses.aspx?id=152'
)
print(response)