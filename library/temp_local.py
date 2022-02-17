from decimal import Decimal

from fruitpal.client import FruitPalClient

client = FruitPalClient(protocol='http', host='localhost', port=8000)
url = client.path('vendors')
response = client.get('vendors')
response.raise_for_status()
#print(response.json())

'''
vendor_database = [
   VendorInDB(country='MX', commodity='mango', variable_overhead=Decimal('1.24')),
   VendorInDB(country='BZ', commodity='mango', variable_overhead=Decimal('1.42'))
]
'''

# result = client.create_vendor(country='MX', commodity='mango', variable_overhead=Decimal('1.24'))
result = client.create_vendor(country='BZ5', commodity='mango', variable_overhead=Decimal('1.42'))
print(result.variable_overhead, result.variable_overhead.__class__)