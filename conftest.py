import random

import pytest

from ingredient_types import *
from services.gen_float_number import generate_random_float
from services.gen_string import generate_random_string


@pytest.fixture(scope="function")
def name():
    name = generate_random_string()
    return name


@pytest.fixture(scope="function")
def price():
    price = generate_random_float()
    return price


@pytest.fixture(scope="function")
def type_ingredient():
    types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING ]
    random_type = random.choice(types)
    return random_type

