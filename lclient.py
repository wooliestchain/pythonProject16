from suds.client import Client
from datetime import datetime
url = 'http://localhost:8000/?wsdl'
client = Client(url)

now = datetime.now().date()
year = now.year
month = now.month
day = now.day

print(now)
response = client.service.recette_a_day("2023-04-28")

print(response)