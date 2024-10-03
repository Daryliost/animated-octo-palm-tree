import os

#1) Add expenses - completed
#2) View expenses - completed
#3) Categorize expenses -
#4) Visualize Data
#5) Export data
#The goal is to allow users to track expenses and categorize and visualize spending habits.

def user_expense() -> None:
    total: float = {}
    while True:
        category: str = input("Please input Category: ")
        expense: float = float(input("Please input expenses, type 'q' to quit: "))
        total += expense
        print(f"Your total amount of expenses is {total}")
        if expense().lower() in ['quit', 'q']:
            break
        elif category().lower in ['quit','q']:
             break
        

def user_input() -> None:
        user_input_str: str = input(str("would you like to input expenses? 'yes' to continue: "))
        if  user_input_str.strip().lower() in ['yes','y','ye']:
            user_expense()
        else: print('Error, not a valid option')
        return

def main() -> None:
    user_input()

if __name__ == '__main__':
    main()