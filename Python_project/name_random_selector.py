import random

names: dict = []
def name_machine() -> None:
    while True:
        global names
        name: str = input("Please input names, 'q' or 'quit' to quit: ")
        if name.strip().lower() in ['q','quit']:
            break
        else:
            names.append(name)
            print(name,'Has been chosen!!!!!\n')

def pick_random_name() -> None:
    global names
    if names:
        print(random.choice(names))
    else:
        print("No names to pick from.")

def create_weird_name() -> None:
    weird_name: list = []
    alphabet: list = list('stinky')
    for _ in alphabet:
        weird_name.append(random.choice(alphabet))
    print("Weird name:", ''.join(weird_name))
        

if __name__ == "__main__":
    name_machine()
    pick_random_name()
    create_weird_name()
    