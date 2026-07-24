from src.category import Category


def test_categori_init(categori_class_init):
    '''Проверяем конструктор класса Category.'''

    assert categori_class_init.name == 'Хозтовары'
    assert categori_class_init.description == 'Приобретаемые хозтовары для стройки.'
    assert categori_class_init.products_list == ['Перчатки', 'Цемент', 'Тачанка']
    assert categori_class_init.category_count == 1
    assert categori_class_init.product_count == 3


def test_add_product(categori_class_init, products_class_init_gloves):
    '''Проверка доьавления в список продуктов объекта категории.'''

    categori_class_init.add_product(products_class_init_gloves)
    assert len(categori_class_init.products_list) == 4


def test_products_name(categori_class_init):
    '''Проверяем геттер products_list.'''
    assert categori_class_init.products_list == ['Перчатки', 'Цемент', 'Тачанка']


def test_products(products_class_init_gloves):
    '''Проверка геттера, который возвращает список продуктов в подготовленной строке.'''
    result = Category('Наименвоание категории', 'Описание', [products_class_init_gloves])
    assert result.products == ['Перчатки, 100 руб. Остаток: 5 шт.']


def test_category_str(categori_class_init_2):
    '''Проверкаа работы магического метода __str__ в классе Category.'''
    assert str(categori_class_init_2) == 'Хозтовары, количество продуктов: 11 шт.'
    assert categori_class_init_2.name == 'Хозтовары'
    assert len(categori_class_init_2.products) == 3


def test_zero_middle_price(capsys):
    '''Тест на проверку пустого списка продуктов в классе Category.'''

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    result = category_empty.middle_price()
    message = capsys.readouterr()
    assert message.out.strip() == 'Отсутствуют продукты для вычисления среднего значения.'
    assert result == 0.0
