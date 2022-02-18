from decimal import Decimal

from fruitpal.client import FruitPalClient

client = FruitPalClient(protocol='http', host='localhost', port=8000)
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