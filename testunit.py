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


def test_apply_discount():
    assert apply_discount(3, 30) == pytest.approx(27.00, abs=1e-2)  # 10% discount
    assert apply_discount(11, 60) == pytest.approx(48.00, abs=1e-2)  # 20% discount
    assert apply_discount(2, 10) == pytest.approx(10.00, abs=1e-2)  # No discount


def test_apply_special_offer_discount():
    assert apply_special_offer_discount(45) == pytest.approx(35.00, abs=1e-2)  # $10 discount
    assert apply_special_offer_discount(120) == pytest.approx(95.00, abs=1e-2)  # $25 discount
    assert apply_special_offer_discount(25) == pytest.approx(25.00, abs=1e-2)  # No discount


def test_apply_special_meal_surcharge(sample_order, sample_menu):
    surcharge = apply_special_meal_surcharge(sample_order, sample_menu)
    assert surcharge == pytest.approx(18.75 * 2 * 0.05, abs=1e-2)  # 5% surcharge for Chef's Special Pasta


def test_validate_meal_availability(sample_order, sample_menu):
    assert validate_meal_availability(sample_order.keys(), sample_menu) is True
    assert validate_meal_availability([0, 2, 4], sample_menu) is False  # Meal 0 and 4 are unavailable


# Additional test cases can be added to further verify the functions


if __name__ == '__main__':
    pytest.main()
