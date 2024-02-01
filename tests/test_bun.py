from bun import Bun


class TestBun:

    def test_get_name_get_expected_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price_get_expected_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
