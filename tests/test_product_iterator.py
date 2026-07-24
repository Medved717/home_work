from src.product_iterator import ProductIterator


def test_product_iterator(categori_class_init_2):
    iterator = ProductIterator(categori_class_init_2)
    assert iterator.index == 0
    assert next(iterator).name == 'Перчатки'
    assert iterator.index == 1
    assert next(iterator).name == 'Цемент'
    assert iterator.index == 2
    assert next(iterator).name == 'Тачанка'
