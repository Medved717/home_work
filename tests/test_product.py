import pytest
from src.product import Product

def test_product_init(products_class_init_gloves, products_class_init_cement, products_class_init_wheelbarrow):
    assert products_class_init_gloves.name == 'Перчатки'
    assert products_class_init_gloves.description == 'Перчатки для работы'
    assert products_class_init_gloves.price == 100.0

    assert products_class_init_cement.name == 'Цемент'
    assert products_class_init_cement.description == 'Цемент для работы'
    assert products_class_init_cement.price == 300.0

    assert products_class_init_wheelbarrow.name == 'Тачанка'
    assert products_class_init_wheelbarrow.description == 'Тачанка для работы'
    assert products_class_init_wheelbarrow.price == 500.0
