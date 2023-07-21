import pytest
from main import (
    calculate_total_cost,
    apply_discount,
    apply_special_offer_discount,
    apply_special_meal_surcharge,
    validate_meal_availability,
)

@pytest.fixture
def sample_order():
    return {
        1: {'quantity': 2, 'price': 8.50},
        3: {'quantity': 3, 'price': 6.75},
        5: {'quantity': 1, 'price': 10.25},
    }


@pytest.fixture
def sample_menu():
    return [
        ("Fried Rice", 8.50, "Chinese Food"),
        ("Spaghetti", 12.99, "Italian Food"),
        ("Cheesecake", 6.75, "Pastries"),
        ("Lasagna", 15.50, "Italian Food"),
        ("Sushi", 10.25, "Japanese Food"),
        ("Chef's Special Pasta", 18.75, "Chef's Specials"),
    ]


def test_calculate_total_cost(sample_order):
    total_cost = calculate_total_cost(sample_order)
    assert total_cost == pytest.approx(8.50 * 2 + 6.75 * 3 + 10.25, abs=1e-2)


def test_validate_meal_availability(sample_order, sample_menu):
    assert validate_meal_availability(sample_order.keys(), sample_menu) is True
    assert validate_meal_availability([0, 2, 4], sample_menu) is False  # Meal 0 and 4 are unavailable

# Additional test cases can be added to further verify the functions
