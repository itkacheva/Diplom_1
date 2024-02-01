import pytest

from ingredient import Ingredient
from ingredient_types import *


class TestIngredient:

    def test_get_price_get_expected_price(self, name, price, type_ingredient):
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        assert ingredient.get_price() == price

    def test_get_name_get_expected_name(self, name, price, type_ingredient):
        ingredient = Ingredient(ingredient_type=type_ingredient, name=name, price=price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('type_ingredient_name', [[INGREDIENT_TYPE_SAUCE], [INGREDIENT_TYPE_FILLING]])
    def test_get_type_get_expected_type(self, name, price, type_ingredient_name):
        ingredient = Ingredient(ingredient_type=type_ingredient_name, name=name, price=price)
        assert ingredient.get_type() == type_ingredient_name
