def display_menu(menu):
    print("Menu:")
    for idx, (meal, price, topic) in enumerate(menu, 1):
        print(f"{idx}. {meal} - {topic} (${price:.2f})")


def get_order(menu):
    order = {}
    while True:
        print("\nEnter meal number and quantity (e.g., 1 2) or 'done' to finish:")
        user_input = input().strip().lower()

        if user_input == 'done':
            break

        try:
            meal_number, quantity = map(int, user_input.split())
            if 0 < meal_number <= len(menu):
                meal, price, topic = menu[meal_number - 1]
                if quantity <= 0:
                    print("Invalid quantity. Quantity should be a positive integer greater than zero.")
                    continue

                if meal_number not in order:
                    order[meal_number] = {'quantity': quantity, 'price': price}
                else:
                    order[meal_number]['quantity'] += quantity

                print(f"{quantity} {meal}(s) added to the order.")
            else:
                print("Invalid meal number. Please enter a valid meal number.")
        except ValueError:
            print("Invalid input. Please enter a valid meal number and quantity.")
    return order


def calculate_total_cost(order):
    total_cost = sum(item['price'] * item['quantity'] for item in order.values())
    return total_cost


def apply_discount(total_quantity, total_cost):
    if total_quantity > 10:
        total_cost *= 0.8  # 20% discount for more than 10 meals
    elif total_quantity > 5:
        total_cost *= 0.9  # 10% discount for more than 5 meals
    return total_cost


def apply_special_offer_discount(total_cost):
    if total_cost > 100:
        total_cost -= 25  # $25 discount for total cost exceeding $100
    elif total_cost > 50:
        total_cost -= 10  # $10 discount for total cost exceeding $50
    return total_cost


def apply_special_meal_surcharge(order, menu):
    special_category = "Chef's Specials"
    surcharge_percentage = 0.05
    special_meals = [meal for meal in order if menu[meal - 1][2] == special_category]

    if special_meals:
        total_surcharge = sum(order[meal]['quantity'] * menu[meal - 1][1] * surcharge_percentage for meal in special_meals)
        return total_surcharge
    return 0


def validate_meal_availability(order, menu):
    unavailable_meals = [meal for meal in order if meal > len(menu) or meal <= 0]
    if unavailable_meals:
        print("Invalid selection: The following meal(s) are unavailable.")
        for meal in unavailable_meals:
            print(f"- Meal {meal}")
        return False
    return True


def dining_experience_manager(menu):
    print("Welcome to the Dining Experience Manager!")
    display_menu(menu)

    order = get_order(menu)
    if not validate_meal_availability(order.keys(), menu):
        return -1

    total_quantity = sum(item['quantity'] for item in order.values())
    base_cost = calculate_total_cost(order)
    total_cost = apply_discount(total_quantity, base_cost)

    special_meal_surcharge = apply_special_meal_surcharge(order, menu)
    total_cost += special_meal_surcharge

    total_cost = apply_special_offer_discount(total_cost)

    print("\nYour order summary:")
    for meal, item in order.items():
        print(f"{item['quantity']} {menu[meal - 1][0]}(s) - ${item['price']:.2f} each")

    print(f"\nTotal quantity: {total_quantity}")
    print(f"Base cost: ${base_cost:.2f}")

    if total_quantity > 5:
        print(f"Discount applied: ${base_cost - total_cost:.2f}")

    if special_meal_surcharge > 0:
        print(f"Special meal surcharge: ${special_meal_surcharge:.2f}")

    if total_cost < base_cost:
        print(f"Special offer discount: ${base_cost - total_cost:.2f}")

    print(f"Total cost: ${total_cost:.2f}")

    user_confirmation = input("Confirm order (yes/no): ").strip().lower()
    if user_confirmation == 'yes':
        return int(total_cost)
    else:
        return -1


# Example Menu (You can customize this with different meals, prices, and topics)
menu_items = [
    ("Fried Rice", 8.50, "Chinese Food"),
    ("Spaghetti", 12.99, "Italian Food"),
    ("Cheesecake", 6.75, "Pastries"),
    ("Lasagna", 15.50, "Italian Food"),
    ("Sushi", 10.25, "Japanese Food"),
    ("Chef's Special Pasta", 18.75, "Chef's Specials"),
]

# Testing the Dining Experience Manager
if __name__ == "__main__":
    total_cost = dining_experience_manager(menu_items)
    if total_cost != -1:
        print(f"\nThank you for ordering! Your total cost is ${total_cost}.")
    else:
        print("\nOrder canceled or invalid input. Please try again.")
