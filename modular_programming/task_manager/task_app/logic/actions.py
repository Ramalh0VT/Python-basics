def create_task():
    task = input("Type your task: ")
    if task == "":
        print("You must type something, the task can't be nothing")

if __name__ == "__main__":
    create_task()