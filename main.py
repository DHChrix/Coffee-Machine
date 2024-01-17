from data import MENU
from data import resources


def calculate(n1, n2, n3, n4):
    return (n1 * 25 + n2 * 10 + n3 * 5 + n4) / 100


# m1= money paid m2 = price
def change(m1, m2):
    return m1 - m2


def check_water(name):
    return MENU[name]["ingredients"]["water"]


def check_milk(name):
    return MENU[name]["ingredients"]["milk"]


def check_coffee(name):
    return MENU[name]["ingredients"]["coffee"]




# What to drink?
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
should_continue = True
money_earned = 0
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        should_continue = False

    elif choice == "report":
        should_continue = False
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money_earned}")

    else:
        # coffee machine has 300 water 200 milk 100beans

        water_used = check_water(choice)
        milk_used = check_milk(choice)
        coffee_used = check_coffee(choice)

        if water_used > water:
            print("Sorry, there is not enough water.")
        elif milk_used > milk:
            print("Sorry, there is not enough milk.")
        elif coffee_used > coffee:
            print("Sorry, there is not enough coffee.")
        else:
            # ask for money
            # Penny : 1 cent Dime : 10 cents Nickel: 5 cents Quarter: 25 cents
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            # if there is enough money to buy it? if there is, what is the change?
            price = MENU[choice]["cost"]
            money_paid = calculate(quarters, dimes, nickles, pennies)
            if money_paid < price:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money_refunded = change(money_paid, price)
                money_refunded = round(money_refunded, 1)
                money_earned += price
                print(f"Here is ${money_refunded} in change.")
                print(f"Here is your {choice}☕️. Enjoy!")
                water -= water_used
                milk -= milk_used
                coffee -= coffee_used
