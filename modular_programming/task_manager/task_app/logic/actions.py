import sys
from task_app.database.storage import store_task, get_all_tasks, save_all_tasks, task_deleter, check_task, display_tasks
def menu():
    while True:
        print("=== TASK MANAGER UTILITY ===")
        choice = input("Options | 1- Add a task | 2- Delete a task | 3- Mark a task as completed | 4- Check current tasks | 5- Quit\n").strip()
        if choice == "1":
            task_addition = input("Type a task to be added\n")
            store_task(task_addition)
        elif choice == "2":
            while True:
                try:
                    while True:
                        task_index = int(input("Type the number of the task you want to be deleted\n").strip().lower())
                        if task_index < 0:
                            print("Invalid number, try again.")
                        else:
                            break
                    task_deleter(task_index)
                    break
                except Exception as e:
                    print(f"An error occurred. Error message: {e}")
        elif choice == "3":
            while True:
                try:
                    while True:
                        task_index = int(input("Type the number of the task you want to be deleted\n").strip().lower())
                        if task_index < 0:
                            print("Invalid number, try again.")
                        else:
                            break
                    check_task(task_index)
                    break
                except Exception as e:
                    print(f"An error occurred. Error message: {e}")
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Quitting...")
            sys.exit()
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    menu()




            




        
        

        
    