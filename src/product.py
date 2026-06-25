
class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, dict_product):
        return cls(dict_product["name"], dict_product["description"], dict_product["price"], dict_product["quantity"])


    @property
    def price(self):
        return self.__price


    @price.setter
    def price(self, price):
         if price <= 0:
             print('Цена не должна быть нулевая или отрицательная')
         else:
             self.__price = price