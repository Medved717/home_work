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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError('Неподходящий тип продукта.')

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
        quentity_product = sum(product.quantity for product in self.products_list)
        return f'{self.name}, количество продуктов: {quentity_product} шт.'

    def __iter__(self):
        return ProductIterator(self)

    def middle_price(self):
        try:
            return sum(product.price for product in self.__products) / len(self.__products)
        except ZeroDivisionError:
            print('Отсутствуют продукты для вычисления среднего значения.')
            return 0.0
