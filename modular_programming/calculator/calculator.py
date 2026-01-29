import operations

def menu():
    print("=== SIMPLE CALCULATOR ===")
    print("Choose an option:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    choice = input("")
    if choice == "1":
        operations.add()
    elif choice == "2":
        operations.sub()
    elif choice == "3":
        operations.mult()
    elif choice == "4":
        operations.div()
    elif choice == "5":
        operations.quit()

while True:
    menu()