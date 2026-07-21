import pytest
from src.smartphone import Smartphone

def test_init_class_smartphone_1(smartphone_1):
    assert smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.quantity == 5
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.model == "S23 Ultra"
    assert smartphone_1.memory == 256
    assert smartphone_1.color == "Серый"


def test_init_class_smartphone_2(smartphone_2):
    assert smartphone_2.name == "Iphone 15"
    assert smartphone_2.description == "512GB, Gray space"
    assert smartphone_2.price == 210000.0
    assert smartphone_2.quantity == 8
    assert smartphone_2.efficiency == 98.2
    assert smartphone_2.model == "15"
    assert smartphone_2.memory == 512
    assert smartphone_2.color == "Gray space"


def test_add_smartphone(smartphone_1, smartphone_2):
    result = smartphone_1 + smartphone_2
    assert result == 2580000.0


def test_mixin_init(capsys, smartphone_1):
    result_print = capsys.readouterr()
    assert "Samsung Galaxy S23 Ultra" in result_print.out
    assert "256GB, Серый цвет, 200MP камера" in result_print.out
    assert '180000.0' in result_print.out
    assert '5' in result_print.out

