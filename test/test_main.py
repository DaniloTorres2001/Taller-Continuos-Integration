import pytest
from main import (
    display_menu,
    get_order,
    calculate_total_cost,
    apply_discount,
    apply_special_meal_surcharge,
    apply_special_offer_discount,
    validate_meal_availability,
)


# Define the example menu as a fixture to reuse it in the tests
@pytest.fixture
def example_menu():
    return [
        ("Fried Rice", 8.50, "Chinese Food"),
        ("Spaghetti", 12.99, "Italian Food"),
        ("Cheesecake", 6.75, "Pastries"),
        ("Lasagna", 15.50, "Italian Food"),
        ("Sushi", 10.25, "Japanese Food"),
        ("Chef's Special Pasta", 18.75, "Chef's Specials"),
    ]


# Test display_menu function
def test_display_menu(capsys, example_menu):
    display_menu(example_menu)
    captured = capsys.readouterr()
    assert "Menu:" in captured.out
    assert "1. Fried Rice - Chinese Food ($8.50)" in captured.out


# Test get_order function


# Test calculate_total_cost function
def test_calculate_total_cost(example_menu):
    order = {1: {'quantity': 2, 'price': 8.50}, 3: {'quantity': 1, 'price': 6.75}}
    total_cost = calculate_total_cost(order)
    assert total_cost == 8.50 * 2 + 6.75


# Test apply_discount function
def test_apply_discount_greater_than_10(example_menu):
    total_cost = 100.00
    total_quantity = 12
    discounted_cost = apply_discount(total_quantity, total_cost)
    assert discounted_cost == 80.00


def test_apply_discount_greater_than_5(example_menu):
    total_cost = 70.00
    total_quantity = 6
    discounted_cost = apply_discount(total_quantity, total_cost)
    assert discounted_cost == 63.00


def test_apply_discount_less_than_5(example_menu):
    total_cost = 40.00
    total_quantity = 4
    discounted_cost = apply_discount(total_quantity, total_cost)
    assert discounted_cost == 40.00


# Test apply_special_meal_surcharge function
def test_apply_special_meal_surcharge(example_menu):
    order = {1: {'quantity': 2, 'price': 8.50}, 6: {'quantity': 3, 'price': 18.75}}
    surcharge = apply_special_meal_surcharge(order, example_menu)
    assert surcharge == 18.75 * 3 * 0.05


def test_apply_special_meal_surcharge_no_special_meals(example_menu):
    order = {1: {'quantity': 2, 'price': 8.50}, 3: {'quantity': 1, 'price': 6.75}}
    surcharge = apply_special_meal_surcharge(order, example_menu)
    assert surcharge == 0


# Test apply_special_offer_discount function
def test_apply_special_offer_discount_greater_than_100(example_menu):
    total_cost = 120.00
    discounted_cost = apply_special_offer_discount(total_cost)
    assert discounted_cost == 120.00 - 25


def test_apply_special_offer_discount_greater_than_50(example_menu):
    total_cost = 60.00
    discounted_cost = apply_special_offer_discount(total_cost)
    assert discounted_cost == 60.00 - 10


def test_apply_special_offer_discount_less_than_50(example_menu):
    total_cost = 40.00
    discounted_cost = apply_special_offer_discount(total_cost)
    assert discounted_cost == 40.00


# Test validate_meal_availability function
def test_validate_meal_availability_valid(example_menu):
    order = {1: {'quantity': 2, 'price': 8.50}, 3: {'quantity': 1, 'price': 6.75}}
    valid = validate_meal_availability(order.keys(), example_menu)
    assert valid is True


def test_validate_meal_availability_invalid(example_menu, capsys):
    order = {1: {'quantity': 2, 'price': 8.50}, 3: {'quantity': 1, 'price': 6.75}, 7: {'quantity': 1, 'price': 15.50}}
    valid = validate_meal_availability(order.keys(), example_menu)
    captured = capsys.readouterr()
    assert valid is False
    assert "Invalid selection: The following meal(s) are unavailable." in captured.out
    assert "- Meal 7" in captured.out




