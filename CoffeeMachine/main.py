# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from data import MENU, resources


#def resource_available(coffee_type):
    # if coffee_type == "espresso":
    #     espresso = {}
    #     espresso['water'] = MENU['espresso']['ingredients']['water']
    #     espresso['coffee'] = MENU['espresso']['ingredients']['coffee']
    #     espresso['cost'] = MENU['espresso']['cost']
    #     print(espresso)
    #     if (resources['water'] > espresso['water']) and (resources['coffee'] > espresso['coffee']):
    #         #print("Take ur coffee")
    #         return True
    #
    # elif coffee_type == 'latte':
    #     latte = {}
    #     latte['water'] = MENU['latte']['ingredients']['water']
    #     latte['coffee'] = MENU['latte']['ingredients']['coffee']
    #     latte['milk'] = MENU['latte']['ingredients']['milk']
    #     latte['cost'] = MENU['latte']['cost']
    #     print(latte)
    #     if ((resources['water'] > latte['water']) and resources['coffee'] > latte['coffee'] and
    #              (resources['milk'] > latte['milk'])):
    #                     #print("Take ur coffee")
    #                     return True
    #
    # elif coffee_type == 'cappuccino':
    #     cappuccino = {}
    #     cappuccino['water'] = MENU['cappuccino']['ingredients']['water']
    #     cappuccino['coffee'] = MENU['cappuccino']['ingredients']['coffee']
    #     cappuccino['milk'] = MENU['cappuccino']['ingredients']['milk']
    #     cappuccino['cost'] = MENU['latte']['cost']
    #     print(cappuccino)
    #     if ((resources['water'] > cappuccino['water']) and resources['coffee'] > cappuccino['coffee'] and
    #             (resources['milk'] > cappuccino['milk'])):
    #         #print("Take ur coffee")
    #         return True


    # else:
    #     if resources['water'] < coffee_type['water']: print("sorry there is not enough water")
    #     elif resources['coffee'] > coffee_type['coffee']: print("sorry there is not enough coffee")
    #     elif resources['milk'] > coffee_type['milk']:print("sorry there is not enough milk")
    #     return False
user_input = input("What would you like? (espresso/latte/cappuccino): ")
if user_input == 'report':
    print(f"water: {resources['water']}ml\nMilk: {resources['milk']}ml\ncoffee: {resources['coffee']}g")
else:
    coffee = MENU[user_input]
    print(coffee)
    print(coffee['ingredients'])
    #resource_available(coffee['ingredients'])


