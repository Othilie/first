
import json 
import xmlrpclib


#products = requests.get("https://e6c36d9dcd69bac22f1c31c4fdfadfe2:e0761d339f1c68673e5a757dc74bf86f@othistore.myshopify.com/admin/products.json")
#todos = json.loads(products.text)
#id= todos["products"][1]["id"]

#print(todos)
#print(products.status_code)


ODOO_URL      = 'https://eiffel1.odoo.com'
ODOO_DB       = 'eiffel1'
ODOO_USER     = 'othilie@eiffel.us'
ODOO_PASSWORD = 'azechoco'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format('https://eiffel1.odoo.com'))

common.version()

print(common.version())

uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL))

models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})


data=""
with open("product-Shopify.json", "r") as file:
	data=json.load(file)


id = str(data["product"]["id"])
title = str(data["product"]["title"])
price = str(data["product"]["price"])
weight = str(data["product"]["weight"])
product_type = str(data["product"]["product_type"])


product_id = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.template', 'create', [{
 'name': title,
  'list_price': price,
   'default_code': id,
    'type': 'product',
  'weight': weight,
    }])