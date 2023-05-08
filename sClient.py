from suds.client import Client
from datetime import datetime

now = datetime.now()
month = now.month


client = Client('http://localhost:8000/?wsdl')



res = client.service.recette_a_product_a_month("fruit",month)
print(res)

