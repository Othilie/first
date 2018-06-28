
import json 
import xmlrpclib
import requests
import ssl


ODOO_URL      = 'https://eiffel1.odoo.com'
ODOO_DB       = 'eiffel1'
ODOO_USER     = 'othilie@eiffel.us'
ODOO_PASSWORD = 'azechoco'

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format('https://eiffel1.odoo.com'),verbose=False, use_datetime=True, 
                             context=ssl._create_unverified_context())

common.version()

print(common.version())

uid = common.authenticate(ODOO_DB, ODOO_USER, ODOO_PASSWORD, {})

models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(ODOO_URL), context=ssl._create_unverified_context())

models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD,
    'res.partner', 'check_access_rights',
    ['read'], {'raise_exception': False})

k0 = 0 

#recuperation des donnees

url1= "https://2bc89922d53228a75d3c1d19801e88db:3161e30cb0b38cabb28fab3aae9ea5f7@othiliestore.myshopify.com/admin/products.json"
s = requests.session()
request1 = requests.Request('GET', url1)
prepared_request1 = s.prepare_request(request1)
response1 = s.send(prepared_request1)
products = json.loads(response1.text)


#compte du nombre de produits
url2 = "https://2bc89922d53228a75d3c1d19801e88db:3161e30cb0b38cabb28fab3aae9ea5f7@othiliestore.myshopify.com/admin/products/count.json"
request2 = requests.Request('GET', url2)
prepared_request2 = s.prepare_request(request2)
response2 = s.send(prepared_request2)
k= response2
nb = json.loads(k.text)
nb = nb['count']
nb = int(nb)

#test sur le nombre de produit
if k0 != nb:
	i=0
#remplissage info chaque produit
	while i<nb:
		title = products["products"][i]["title"]
		id= str(products["products"][i]["id"])
		price = str(products["products"][i]["variants"][0]["price"])
		#product_type = str(products["products"][i]["product_type"])
		vendor = str(products["products"][i]["vendor"])
		weight = long(products["products"][i]["variants"][0]["weight"])	
		
		product_id = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.template', 'create', [{
 		'name': title,
  		'list_price': price,
   		'default_code': id,
    	'type': 'product',
  		'weight': weight,
    	}])

		i=i+1
		k0 = nb	


