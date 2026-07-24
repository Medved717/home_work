from abc import ABC, abstractmethod
from src.mixin_product import MixinProduct


class BaseProduct(ABC):

    @abstractmethod
    def __add__(self):
        pass


class Product(BaseProduct, MixinProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.name = name
        self.description = description
        self.__price = price
        if not quantity <= 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')

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

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        summ_products = (self.quantity * self.price) + (other.quantity * other.__price)
        return summ_products
