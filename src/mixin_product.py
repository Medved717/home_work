class MixinProduct:

    def __init__(self, name, description, price, quantity):
        print(f"{self.__class__.__name__}({name}, {description}, {price}, {quantity})")
