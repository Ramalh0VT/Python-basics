def store(task_to_be_added):
    with open ("tasks.txt", "a") as f:
        list_of_tasks = f
        list_of_tasks.append(task_to_be_added)
        print("Task added sucessfully!")


if __name__ == "__main__":
    pife = "PERA AKJ"
    store(pife)
        