from app import db
from models.Product import Product

print('tables: ', db.tables)
print('db: ', db)
print('products columns ', db['products'].columns )
print('how much in table products of db: ', len(db['products']))

table = db['products']
print('find id "1" ', table.find(id=1))

print('test for all in products tables')
for product in table:
    np =  Product.dict_class(product)
    print(np.to_dict())


print('get all in table products')
print(table.all())

print('deleting item novo')
print(table.delete(name='novo'))