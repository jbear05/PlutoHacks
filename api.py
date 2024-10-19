import requests
import json

response = requests.get(f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json")


# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())