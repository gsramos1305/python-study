from menu import MENU, resources


def is_resources_enough(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print("Sorry, insufficient ingredients.")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/capuccino/report/off): ").lower()
    confirm = input("Confirm? y/n: ")
    if confirm == 'y':
        if choice == "off":
            is_on = False
        elif choice == "report":
            for n in resources:
                print(f"{n}: {resources[n]}")
        elif choice == "espresso" or "latte" or "cappuccino":
            for n in MENU[choice]["ingredients"]:
                print(f"{n}: {MENU[choice]['ingredients'][n]}ml")
            drink = MENU[choice]["ingredients"]








