from src.product import Product
import pytest
from src.smartphone import Smartphone


def test_product_init(products_class_init_gloves, products_class_init_cement, products_class_init_wheelbarrow):
    '''Проверка конструктора класса Product'''

    assert products_class_init_gloves.name == 'Перчатки'
    assert products_class_init_gloves.description == 'Перчатки для работы'
    assert products_class_init_gloves.price == 100.0

    assert products_class_init_cement.name == 'Цемент'
    assert products_class_init_cement.description == 'Цемент для работы'
    assert products_class_init_cement.price == 300.0

    assert products_class_init_wheelbarrow.name == 'Тачанка'
    assert products_class_init_wheelbarrow.description == 'Тачанка для работы'
    assert products_class_init_wheelbarrow.price == 500.0


def test_new_product(dict_product):
    '''Проверка метода new_product при создании нового экземпляра из словаря.'''

    result = Product.new_product(dict_product)
    assert result.name == 'Samsung Galaxy S23 Ultra'
    assert result.description == '256GB, Серый цвет, 200MP камера'
    assert result.price == 180000.0
    assert result.quantity == 5


def test_price(dict_product):
    '''Проверка геттера price.'''

    result = Product.new_product(dict_product)
    assert result.price == 180000.0


def test_price_setter(dict_product_price_zero, capsys):
    '''Проверка геттера products при выводе сообщения в консоль.'''

    result = Product.new_product(dict_product_price_zero)

    result.price = 0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert result.price == 500.0


def test_str_product(products_class_init_cement, products_class_init_wheelbarrow):
    '''Проверкаа работы магического метода __str__ в классе Product.'''

    assert str(products_class_init_cement) == 'Цемент, 300 руб. Остаток: 5 шт.'
    assert str(products_class_init_wheelbarrow) == 'Тачанка, 500 руб. Остаток: 1 шт.'


def test_add_product(products_class_init_gloves, products_class_init_cement, products_class_init_wheelbarrow):
    '''Проверка работы класса MixinProduct.'''

    assert products_class_init_gloves + products_class_init_cement == 2000
    assert products_class_init_gloves + products_class_init_wheelbarrow == 1000
    assert products_class_init_cement + products_class_init_wheelbarrow == 2000


def test_zero_quentity():
    '''Тест на проверку нулевого значения количества товаров.'''

    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Smartphone("Iphone 15", "512GB, Gray space", 210000.0,
                   0, 98.2, "15", 512, "Gray space")
