# import another_module
# print(another_module.another_variable)
# from another_module import another_variable
# print(another_variable)
#
# import turtle
# timmy = turtle.Turtle()
# import turtle
# from turtle import Turtle,Screen # importing the class Turtle from module turtle
# timmy = Turtle() # creating an object of Turtle class
# print(timmy) # <turtle.Turtle object at 0x000001C5FEBBB1F0> So its an object that getting printed
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight) #accessing Screen attribute
# my_screen.exitonclick() #accessing Method, the screen exits after clicking on it only
#import prettytable # to see the code - r8 click on prettytable=>go to => implementations
from prettytable import PrettyTable
table = PrettyTable()
#create the table with data
table.field_names = ["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu", 'Electric'],
        ["Sqirtle", 'Water'],
        ["Charmandar", 'Fire'],
    ]
)
print(table)
