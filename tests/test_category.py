import pytest

from src.category import Category


def test_categori_init(categori_class_init):
    assert categori_class_init.name == 'Хозтовары'
    assert categori_class_init.description == 'Приобретаемые хозтовары для стройки.'
    assert categori_class_init.products_name == ['Перчатки', 'Цемент', 'Тачанка']
    assert categori_class_init.category_count == 1
    assert categori_class_init.product_count == 3


