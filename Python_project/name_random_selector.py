import random

names: dict = []
def name_machine() -> None:
    while True:
        global names
        name = input("Please input names, 'q' or 'quit' to quit: ")
        if name.strip().lower() in ['q','quit']:
            break
        else:
            names.append(name)
            print(name,'\n')

def pick_random_name() -> None:
    global names
    if names:
        print(random.choice(names))
    else:
        print("No names to pick from.")

def create_weird_name() -> None:
    global names
    for name in names:
        random.choice(['A', 'E', 'I', 'O', 'U'])
        print (names)

if __name__ == "__main__":
    name_machine()
    pick_random_name()
    