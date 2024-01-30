import pytest

from burger import Burger
from mocks.mock_ingredient import set_mock_ingredient

from mocks.mock_bun import set_mock_bun
from services.gen_float_number import generate_random_float
from services.gen_string import generate_random_string


class TestBurger:

    def test_set_buns_set_buns_success(self, name, price):
        mock_bun = set_mock_bun(name, price)
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun.get_name() == name and burger.bun.get_price() == price

    def test_add_ingredient_add_given_ingredient(self, name, price):
        mock_ingredient = set_mock_ingredient(name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient_given_ingredient_remove(self, name, price):
        mock_ingredient = set_mock_ingredient(name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_get_price_get_expected_price(self):
        price_bun = generate_random_float()
        price_ingredient = generate_random_float()
        calc_price = price_bun*2 + price_ingredient

        mock_bun = set_mock_bun(name=generate_random_string(), price=price_bun)
        mock_ingredient = set_mock_ingredient (name=generate_random_string(), price=price_ingredient)

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == calc_price

    @pytest.mark.parametrize('name_bun, price_bun, name_ingredient, price_ingredient',
                             [['черная булочка', '150.20', 'салат', '10.25']])
    def test_get_receipt_contains_specified_parameters(self, name_bun, price_bun, name_ingredient, price_ingredient):
        mock_bun = set_mock_bun(name=name_bun, price=price_bun)
        mock_ingredient = set_mock_ingredient(name=name_ingredient, price=price_ingredient)

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        receipt = burger.get_receipt()

        assert receipt.find(name_bun) != -1 \
               and receipt.find(price_bun) != -1 \
               and receipt.find(name_ingredient) != -1 \
               and receipt.find(price_ingredient) != -1
