import urllib.request
import json 
import requests

#with open("product.json", "r") as read_file:
   # data=json.load(read_file)

#data_json = json.dumps(data)

url = "https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/custom_products.json"

datas = {
  "product": {
    "title": "Burton Custom Freestyle 1512",
    "body_html": "<strong>Good snowboard!</strong>",
    "vendor": "Burton",
    "product_type": "Snowboard",
    "tags": "Barnes & Noble, John's Fav, \"Big Air\""
  }
}

data = ""

with open("connect.json", "r") as read_file:
    data=json.load(read_file)

print(data)

headers = {'Content-type': 'application/json'}

#rsp = requests.post(url, json=datas, headers=headers)

r = requests.post("https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products.json", json=datas, headers=headers)

