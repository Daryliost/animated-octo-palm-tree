while True:
    names = {}
    names = input("Please input names: ")
    if names.strip().lower() in ['n','no']:
        break
    else: print(f"{names}")
