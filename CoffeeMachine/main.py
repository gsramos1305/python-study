from menu import MENU

machine_working = True
while machine_working:
    ask_user = input("What would you like? (espresso/latte/capuccino): ")
    for n in MENU[ask_user]["ingredients"]:
        print(f"{n}: {MENU[ask_user]['ingredients'][n]}ml")


