import data_fetcher
def convert():
    choice_1 = input("Hello! What city do you wish to know the temperature? ").strip().lower()
    info = data_fetcher.data()
    if choice_1 in info["city"]:
        index = info["city"].index(choice_1) 
        result = info["temperature_c"][index]
    else:
        result = None

    if result:
        choice_2 = input("Would you like to see the temperature on celsius or fahrenheit? (c/f)").strip().lower()
        if choice_2 == "f":
            fahrenheit(result)
            print(f"The temperature in {choice_1} is ")
    else:
        print("City not found in the database. Would you like to try again? (y/n)")
        while True:
            continue_option = input("")
            if continue_option == "y":
                convert()
                break
            elif continue_option == "n":
                print("Okay, returning to the main menu...")
                return
            else:
                print("Invalid option. The valid options are 'y' and 'n'. ")
    
            


convert()
    

