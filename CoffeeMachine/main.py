from menu import MENU, resources


def is_resources_enough(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] >= resources[item]:
            print(f"Sorry, insufficient {item}.")
            print("\n"*2)
            return False
    return True

def process_coins():
    print("---Insert coins---")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.10
    total += int(input("Nickels: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"\nYour change: ${change:.2f}")
        return True
    else:
        print("Not enough money.")
        print("\n"*2)
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}!")
    print("\n"*2)

is_on = True
while is_on:
    print("\n")
    print("MENU: ")
    for drink in MENU:
        print(f"-{drink}: ${MENU[drink]['cost']}")
    choice = input("\nWhat would you like?: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        for n in resources:
              print(f"{n}: {resources[n]}")
    elif choice == "espresso" or "latte" or "cappuccino":
          #for n in MENU[choice]["ingredients"]:
              #print(f"{n}: {MENU[choice]['ingredients'][n]}ml")
          drink = MENU[choice]
          if is_resources_enough(drink["ingredients"]):
              user_money = process_coins()
              print(f"\nMoney inserted: ${user_money:.2f}")
              confirm = input("Confirm? y/n: ")
              if confirm == 'y':
                  if is_transaction_successful(user_money, drink["cost"]):
                      make_coffee(choice, drink["ingredients"])











