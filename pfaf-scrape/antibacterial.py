import requests
response = requests.get(
    'https://pfaf.org/user/Search_Use.aspx?glossary=Antibacterial'
)
print(response)
