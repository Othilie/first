import xmlrpclib

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

data = input('data:')
data = data.split(" ")
print(data)

sku = data[data.index("sku:") + 1]
price = float(data[data.index("price:") + 1])
weight = float(data[data.index("weight:") + 1])


product_id = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'product.template', 'create', [{
    'name': data[1],
    'list_price': price,
    'default_code': sku,
    'type': 'product',
    'weight': weight,
    }])


