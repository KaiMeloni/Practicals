menu = """S - Shop
L - Leave
Q - Quit"""
print(menu)
name = int(input("What is your name: "))
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "S":
        print("hello", name)
    elif choice == "L":
        print("goodbye", name)
    else:
        print("Invalid input")
    print(menu)
    choice = input(">>> ").upper()
print("Finished")
