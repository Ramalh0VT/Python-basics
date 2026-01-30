import data_fetcher
import formatter
import sys
def quit_app():
    print("Quitting... ")
    sys.exit()

def menu():
    while True:
        print("=== WEATHER DASHBOARD APPLICATION ===") 
        print("Choose an option:")
        print("1- See the database to check for available cities to check temperature")
        print("2- Check a city temperature")
        print("3- Quit")
        choice = input("").strip()
        if choice == "1":
            value = data_fetcher.data()
            print("Here is the database of available cities:")
            print(", ".join(value.keys()))
        elif choice == "2":
            formatter.temp()
        elif choice == "3":
            quit_app()
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
    
