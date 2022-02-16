from fruitpal.client import FruitPalClient

client = FruitPalClient(base_url='http://localhost:8000')
url = client.path('vendors')
response = await client._get('vendors')
print(response)