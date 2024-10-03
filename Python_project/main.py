#1) Add expenses - completed
#2) View expenses - completed
#3) Categorize expenses - completed
#4) Visualize Data - cannot do unless install a different python library, trying to keep it on default python
#5) Export data - working
#The goal is to allow users to track expenses and categorize and visualize spending habits.

def user_expense() -> None:
    total: dict = {}
    while True:
        category: str = input("Please input category, type 'q' to quit: ").strip()
        if category.lower() in ['quit', 'q']:
            break

        expense_input: str = input("Please input expenses, type 'q' to quit: ").strip()
        if expense_input.lower() in ['quit', 'q']:
            break

        try:
            expense: int = int(expense_input)
        except ValueError:
            print("Invalid expense amount. Please enter a number.")
            continue

        if category in total:
            total[category] += expense
        else:
            total[category] = expense

        print(f"Your total amount of expenses for category {category} is {total[category]}.")
        

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