import json
import re
import urllib.request
import requests

#data=""
#with open("product.json", "r") as file:
#	data=json.load(file)
#data= str(data)

products = requests.get("https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products.json")
data = json.loads(products.text)
#id= todos["products"][1]["id"]
#print(data)
#id = data["product"]["id"]
data = str(data)

name = input("title?")
data1 = data.split("images")
#data = data.split(":")
print(data1[0])
k= requests.get("https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products/count.json")
nb = json.loads(k.text)
nb = nb['count']
nb = int(nb)
i=0
while i<nb:
	index = str(data1[i]).find(name)
	if index > -1:
		print(i)
		break
	i = i + 1
#name = data[data.index("id")]

#data=""
#with open("product.json", "r") as file:
#	data=json.load(file)
#data= str(data)
products = requests.get("https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products.json")
todos = json.loads(products.text)
id= todos["products"][i]["id"]
print(id)

def sku():
	code = id
	return(code)


