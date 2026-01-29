import sys

def add():
    final_result = 0
    while True:
        try:
            num_of_numbers = int(input("How many numbers do you want to add?(Must a number greater than 1, don't type the whole number, just the number. e.g: 0, 1, 2, etc.): "))
            if num_of_numbers <= 1:
                print("Number is equal or lower than 1")
                continue
            break
        except Exception as e:
             print(f"Invalid input, an error occured. Error message:{e}")

    while True:
        if num_of_numbers == 0:
            break
        for i in range(num_of_numbers):
            try:
                i = input("Type a number to be added:(don't write the number in words. Enter q to stop adding.)").strip().lower()
                if i == "q":
                    print("Returning to the menu...")
                    return None
                i_int = int(i)
                final_result += i_int
                num_of_numbers -= 1
            except:
                print("Invalid value, try again")
                continue
    print(f"The result is: {final_result}")

def sub():
    final_result = 0
    while True:
        try:
            num_of_numbers = int(input("How many numbers do you want to subtract?(Must a number greater than 1, don't type the whole number, just the number. e.g: 0, 1, 2, etc.): "))
            if num_of_numbers <= 1:
                print("Number is equal or lower than 1")
                continue
            break
        except Exception as e:
             print(f"Invalid input, an error occured. Error message:{e}")

    while True:
        if num_of_numbers == 0:
            break
        for i in range(num_of_numbers):
            try:
                i = input("Type a number to be subtracted:(don't write the number in words. Enter q to stop subtracting.)").strip().lower()
                if i == "q":
                    print("Returning to the menu...")
                    return None
                i_int = int(i)
                final_result -= i_int
                num_of_numbers -= 1
            except:
                print("Invalid value, try again")
                continue
    print(f"The result is: {final_result}")

def mult():
    final_result = 0
    while True:
        try:
            num_of_numbers = int(input("How many numbers do you want to multiply?(Must a number greater than 1, don't type the whole number, just the number. e.g: 0, 1, 2, etc.): "))
            if num_of_numbers <= 1:
                print("Number is equal or lower than 1")
                continue
            break
        except Exception as e:
             print(f"Invalid input, an error occured. Error message:{e}")

    while True:
        if num_of_numbers == 0:
            break
        for i in range(num_of_numbers):
            try:
                i = input("Type a number to be multiplied:(don't write the number in words. Enter q to stop multiplying.)").strip().lower()
                if i == "q":
                    print("Returning to the menu...")
                    return None
                i_int = int(i)
                final_result *= i_int
                num_of_numbers -= 1
            except:
                print("Invalid value, try again")
                continue
    print(f"The result is: {final_result}")

def div():
    final_result = 0
    while True:
        try:
            num_of_numbers = int(input("How many numbers do you want to divide?(Must a number greater than 1, don't type the whole number, just the number. e.g: 0, 1, 2, etc.): "))
            if num_of_numbers <= 1:
                print("Number is equal or lower than 1")
                continue
            break
        except Exception as e:
             print(f"Invalid input, an error occured. Error message:{e}")

    while True:
        if num_of_numbers == 0:
            break
        for i in range(num_of_numbers):
            try:
                i = input("Type a number to be divided:(don't write the number in words. Enter q to stop dividing.)").strip().lower()
                if i == "q":
                    print("Returning to the menu...")
                    return None
                i_int = int(i)
                final_result /= i_int
                num_of_numbers -= 1
            except:
                print("Invalid value, try again")
                continue
    print(f"The result is: {final_result}")

def quit():
    print("Quitting...")
    sys.exit()


