import os

#1.) Add expenses
#2.) View expenses
#3.) Categorize expenses
#4.) Visualize Data
#5.) Export data
#The goal is to allow users to track expenses and categorize and visualize spending habits.

#clearly defining functions
def user_expense():
    total = 0


print("welcome to Daryl\'s expense calculaton.\nPlease press '1' to add expenses\nPlease press '2' to view expenses\nPlease press '3' to vizualize your expenses.\nPress '5' to export your data")








user_input = input().strip().lower()
if user_input in ['yes','y','ye']:
    user_expense()