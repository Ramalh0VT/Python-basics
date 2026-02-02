import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "tasks_data.txt")

def store_task(task_to_be_added):
    try:
        with open(FILE_PATH, "a") as f:
            
            f.write(f"[ ] {task_to_be_added}\n")
            print("Task added successfully!")
    except Exception as e:
        print(f"Error saving task: {e}")

def get_all_tasks():
    
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return f.readlines()

def save_all_tasks(tasks):
    
    with open(FILE_PATH, "w") as f:
        f.writelines(tasks)

def task_deleter(index):
    tasks = get_all_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_all_tasks(tasks)
        print(f"Deleted: {removed.strip()}")
    else:
        print("Invalid task number.")

def check_task(index):
    tasks = get_all_tasks()
    if 0 <= index < len(tasks):
        
        tasks[index] = tasks[index].replace("[ ]", "[X]", 1)
        save_all_tasks(tasks)
        print("Task marked as complete!")
    else:
        print("Invalid task number.")

def display_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print("No tasks found.")
    for i, task in enumerate(tasks):
        print(f"{i}. {task.strip()}")

if __name__ == "__main__":
    
    print("Placeholder")