from 

def create_task():
    while True:
        task = input("Type your task: \n")
        if task == "":
            print("You must type something, the task can't be nothing")
        else:
            break
        
    
def remove_task():
    while True:
        task_to_remove = input("Type the task you want to be removed: \n")
        if task_to_remove = "":
            print("You must type something, you can't remove an empty task.")
        else:
            break

if __name__ == "__main__":
    create_task()