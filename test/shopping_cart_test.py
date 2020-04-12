# shopping-cart/test/shopping_cart_test.py

from app.shopping_cart import to_usd

def test_to_usd():
    price = 12.5
    price_usd = to_usd(price)
    assert price_usd == "$12.50"

    # it should apply USD formatting
    assert to_usd(12.50) == "$12.50"

    # it should display two decimal places
    assert to_usd(12.5) == "$12.50"

    # it should round to two places
    assert to_usd(12.52345) == "$12.52"

    # it should display thousands separators
    assert to_usd(1234567890) == "$1,234,567,890.00"