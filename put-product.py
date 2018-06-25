import urllib.request
import json 
import requests

from read_id_json import sku
id = sku()

from read_id_json import data
datas = data()

url = "https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products/"
url2= id
url3= ".json"
url5= "%s%s%s"%(url,url2,url3)

print(url5)
print(datas)



data1 = {
 "product": 
    datas
 
 }

data1["product"]["variants"][0]["price"] = "300.00"

headers = {'Content-type': 'application/json'}

#rsp = requests.post(url, json=datas, headers=headers)

r = requests.put(url5, json=data1)
print(r.status_code)