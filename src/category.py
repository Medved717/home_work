from src.product import Product

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


    @property
    def products_name(self):

        return self.__products


    @property
    def products(self):
        list_products = []

        for product in self.__products:
            list_products.append(f'{product.name}, {product.price} руб. {product.quantity}: 15 шт.')

        return list_products







