from Menu import MENU, resources

coffee_machine_resources = resources
coffee_machine_resources['cost'] = 0


def user_choice(choice, coffee_machine_resources):
    """If user type a 'report' then it shows what is inside"""
    if choice == 'report':
        print(f"Water: {coffee_machine_resources['water']}\n"
              f"Milk: {coffee_machine_resources['milk']}\n"
              f"Coffee: {coffee_machine_resources['coffee']}\n"
              f"Money: ${coffee_machine_resources['cost']}")


def check_resources(machine_resources, users_coffee, choice):
    """Check if ingredients are enough to make a coffee"""
    if choice == "espresso":
        if machine_resources['water'] >= users_coffee['ingredients']['water']:
            if machine_resources['coffee'] >= users_coffee['ingredients']['coffee']:
                return True
    else:
        if machine_resources['water'] >= users_coffee['ingredients']['water']:
            if machine_resources['milk'] >= users_coffee['ingredients']['milk']:
                if machine_resources['coffee'] >= users_coffee['ingredients']['coffee']:
                    return True
    return False


def process_coins():
    """Return the total calculated from coins inserted."""
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(users_money, coffee_costs):
    """Check if user have enough money to buy a coffee"""
    if users_money == coffee_costs:
        return True
    elif users_money > coffee_costs:
        users_money -= coffee_costs
        print(f"Here is ${round(users_money, 2)} in change.")
        return True
    else:
        return False


def coffee_machine():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        while choice == 'report':
            user_choice(choice, coffee_machine_resources)
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == 'off':
            exit()

        users_coffee = MENU[choice]
        coffee_costs = MENU[choice]['cost']

        is_sufficient = check_resources(coffee_machine_resources, users_coffee, choice)

        if is_sufficient:
            payment = process_coins()
            is_money_enough = check_transaction(payment, coffee_costs)

            if is_money_enough:
                if choice == 'espresso':
                    coffee_machine_resources['water'] -= users_coffee['ingredients']['water']
                    coffee_machine_resources['coffee'] -= users_coffee['ingredients']['coffee']
                    coffee_machine_resources['cost'] += users_coffee['cost']
                else:
                    coffee_machine_resources['water'] -= users_coffee['ingredients']['water']
                    coffee_machine_resources['milk'] -= users_coffee['ingredients']['milk']
                    coffee_machine_resources['coffee'] -= users_coffee['ingredients']['coffee']
                    coffee_machine_resources['cost'] += users_coffee['cost']
                print(f"Here is your {choice} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")


coffee_machine()