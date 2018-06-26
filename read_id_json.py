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
data = str(data)

name = input("title?")
data1 = data.split("images")
#print(data1[0])
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
price = todos["products"][i]["variants"][0]["price"]
product_type = todos["products"][i]["product_type"]
vendor = todos["products"][i]["vendor"]
weight = todos["products"][i]["variants"][0]["weight"]


dico = {"product": 
	{"title": name, 
	"id":id,
	#"body_html": "<strong>Good snowboard!</strong>", 
	"vendor": vendor, 
	"product_type": product_type, 
	"price": price,
	"weight": weight,
	#"tags": "Barnes & Noble, John's Fav, \"Big Air\""
	}
}

with open("product-Shopify.json", "w") as f_write:
    json.dump(dico, f_write)

def data():
	return(todos["products"][i])

def sku():
	return(id)

def name():
	return(name)

def price():
	return(price)


