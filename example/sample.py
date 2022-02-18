from fruitpal.client import FruitPalClient

client = FruitPalClient.from_url('http://localhost:8000/api/v1')

for vendor in client.read_vendors(commodity='mango'):
    print(vendor)

for estimate in client.estimate(commodity='mango', unit_price=53, volume=405):
    print(estimate)
