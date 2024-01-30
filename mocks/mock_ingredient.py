from unittest.mock import Mock

from ingredient_types import INGREDIENT_TYPE_SAUCE


def set_mock_ingredient(name, price):
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = price
    mock_ingredient.get_name.return_value = name
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE

    return mock_ingredient


