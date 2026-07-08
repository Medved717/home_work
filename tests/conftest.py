import pytest

from lawn_grass import LawnGrass
from src.category import Category
from src.product import Product


@pytest.fixture
def categori_class_init():
    return Category(
        'Хозтовары', 'Приобретаемые хозтовары для стройки.',
                    ['Перчатки', 'Цемент', 'Тачанка']
    )

@pytest.fixture
def products_class_init_gloves():
    return Product(
        'Перчатки', 'Перчатки для работы', 100, 5
    )

@pytest.fixture
def products_class_init_cement():
    return Product(
        'Цемент', 'Цемент для работы', 300, 5
    )

@pytest.fixture
def products_class_init_wheelbarrow():
    return Product(
        'Тачанка', 'Тачанка для работы', 500, 1
    )

@pytest.fixture
def dict_product():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5}


@pytest.fixture
def dict_product_price_zero():
    return {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 500,
         "quantity": 5}


@pytest.fixture
def categori_class_init_2(products_class_init_gloves, products_class_init_cement, products_class_init_wheelbarrow):
    return Category(
        'Хозтовары', 'Приобретаемые хозтовары для стройки.',
        [products_class_init_gloves,
                 products_class_init_cement,
                 products_class_init_wheelbarrow])


@pytest.fixture()
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")