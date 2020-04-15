# shopping-cart/test/shopping_cart_test.py

from app.shopping_cart import TAX_RATE, to_usd, print_selection

def test_tax_rate():
    assert(TAX_RATE) == 0.0875


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

def test_print_selection():
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99}
    ]

    selected_ids = ["1", "2"]
    subtotal = 0

    subtotal = print_selection(selected_ids, products, subtotal, None)
    assert subtotal == 8.49
