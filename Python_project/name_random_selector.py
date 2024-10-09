import random

names: list = []
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

def create_weird_name() -> str:
    global names
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    weird_names = []
    for name in names:
        weird_name = ''.join(random.choice(alphabet) for _ in name)
        weird_names.append(weird_name)
    return ' '.join(weird_names)
    

if __name__ == "__main__":
    name_machine()
    pick_random_name()
    weird_name: str = create_weird_name()
    print(f"\nWeird name: {weird_name}")