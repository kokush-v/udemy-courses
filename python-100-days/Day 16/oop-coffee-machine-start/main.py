from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
coffe_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

def main():
    print(f"Coffe machine stats:")
    coffe_maker_obj.report()

    choice = input(f"What coffe do you want: {menu_obj.get_items()}\n")
    drink = menu_obj.find_drink(choice)
    can_make_coffe = coffe_maker_obj.is_resource_sufficient(drink)

    if can_make_coffe:
        payment_success = money_machine_obj.make_payment(drink.cost)
        money_machine_obj.report()

        if payment_success:
            coffe_maker_obj.make_coffee(drink)

    else:
        print("Maybe you could select another drink")


while True:
    choice = input("What you want do next:\ninsert coins (1)\nmake coffe (2)\nturn off (3)\n")
    if choice == "1":
        money_machine_obj.process_coins()
    elif choice == "2":
        main()
    elif choice == "3":
        break



