import urllib.request
import json 
import requests

#with open("product.json", "r") as read_file:
 #   data=json.load(read_file)
#data_json = json.dumps(data)
#payload = {'json_payload': data_json}
#products = requests.get("https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products.json")
#todos = json.loads(products.text)
#id= todos["products"][1]["id"]
#print(id)

from read_id_json import sku
id = sku()

url = "https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products/"
url2= id
url3= ".json"
url5= "%s%s%s"%(url,url2,url3)
print(url5)

headers = {'Content-type': 'application/json'}

#rsp = requests.post(url, json=datas, headers=headers)

r = requests.delete(url5, json=None, headers=headers)

print(r.status_code)