from decimal import Decimal

from fruitpal.client import FruitPalClient

# client = FruitPalClient(scheme='http', host='localhost', port=8000, prefix='/api/v1')
client = FruitPalClient.from_url('http://localhost:8000/api/v1')
print(client.base_url)

for vendor in client.read_vendors(commodity='mango'):
    print(vendor)

'''
vendor_database = [
   VendorInDB(country='MX', commodity='mango', variable_overhead=Decimal('1.24')),
   VendorInDB(country='BZ', commodity='mango', variable_overhead=Decimal('1.42'))
]
'''

# result = client.create_vendor(country='MX', commodity='mango', variable_overhead=Decimal('1.24'))
# result = client.create_vendor(country='BZ', commodity='mango', variable_overhead=Decimal('1.42'))
# print(result)

for estimate in client.estimate(commodity='mango', unit_price=53, volume=405):
    print(estimate)