# test_checkout.py

# from pytest_bdd import scenario, given, when, then
from pytest_bdd import scenario, given, when, then
from store import ShoppingCart

# def test_cart_has_no_items():
#     cart=ShoppingCart()
#     assert len(cart.items) == 0

# def test_add_item_to_cart():
#     cart=ShoppingCart()
#     cart.add_item('Tool Box')
#     assert len(cart.items) == 1

@scenario('checkout.feature', 'Applying a discount code')
def test_apply_discount():
    pass

@given('the customer has items in the cart')
def customer_cart():
    cart = ShoppingCart()
    cart.add_item('book', 1)
    return cart

@when('they apply a discount code')
def apply_discount(customer_cart):
    customer_cart.apply_discount('DISCOUNT10')

@then('the total price should reflect the discount')
def check_total(customer_cart):
    assert customer_cart.total == 9.0 # Assuming the discount is 10%