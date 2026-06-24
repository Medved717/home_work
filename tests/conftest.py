import pytest
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