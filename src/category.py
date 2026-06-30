from src.product import Product
from src.product_iterator import ProductIterator


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    # Не уверен, что данный код нужен, просто хотел оставить геттер, который просто возвращает атрибут????
    @property
    def products_list(self):
        return self.__products

    @property
    def products(self):
        list_products = []

        for product in self.__products:
            list_products.append(f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.')

        return list_products

    def __str__(self):
        return f'{self.name}, количество продуктов: {self.product_count} шт.'

    def __iter__(self):
        return ProductIterator(self)






