from app import db

class Product:
    def __init__(self, name, buy_price=0, sell_price=0, qtd=0):
        self.name = name
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.qtd = qtd

    def to_dict(self):
        print(dict(name=self.name, buy_price=self.buy_price, sell_price=self.sell_price, qtd=self.qtd))
        return dict(name=self.name, buy_price=self.buy_price, sell_price=self.sell_price, qtd=self.qtd)

    @staticmethod
    def dict_class(product):
        return Product(product['name'], product['buy_price'], product['sell_price'], product['qtd'])

    def save(self):
        db['products'].insert(self.to_dict())