import os

#1.) Add expenses
#2.) View expenses
#3.) Categorize expenses
#4.) Visualize Data
#5.) Export data
#The goal is to allow users to track expenses and categorize and visualize spending habits.

def user_expense():
    print('Please input expenses')
    input(int())

print('Would you like to input expenses?')
user_input = input(str())
if  user_input == 'yes':
    user_expense() 