def test_init_class_lawn_grass_1(grass_1):
    assert grass_1.name == "Газонная трава"
    assert grass_1.description == "Элитная трава для газона"
    assert grass_1.price == 500.0
    assert grass_1.quantity == 20
    assert grass_1.country == "Россия"
    assert grass_1.germination_period == "7 дней"
    assert grass_1.color == "Зеленый"


def test_init_class_lawn_grass_2(grass_2):
    assert grass_2.name == "Газонная трава 2"
    assert grass_2.description == "Выносливая трава"
    assert grass_2.price == 450.0
    assert grass_2.quantity == 15
    assert grass_2.country == "США"
    assert grass_2.germination_period == "5 дней"
    assert grass_2.color == "Темно-зеленый"


def test_add_lawn_grass(grass_1, grass_2):
    result = grass_1 + grass_2
    assert result == 16750.0
