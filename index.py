import os

# Function to clear the terminal

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the to-do list

def display_todo_list(todo_list):
    clear_terminal()
    print("\033[1;34m" + "=" * 30 + "\033[0m")
    print("\033[1;32m" + "      My Unique To-Do List" + "\033[0m")
    print("\033[1;34m" + "=" * 30 + "\033[0m")
    if not todo_list:
        print("\033[1;31m" + "      No tasks added!" + "\033[0m")
    else:
        for idx, task in enumerate(todo_list, start=1):
            print(f"\033[1;33m{idx}. {task}\033[0m")
    print("\033[1;34m" + "=" * 30 + "\033[0m")

# Main program

def main():
    todo_list = []
    while True:
        display_todo_list(todo_list)
        print("\033[1;35m1. Add Task\033[0m")
        print("\033[1;36m2. Remove Task\033[0m")
        print("\033[1;37m3. Exit\033[0m")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter your task: ")
            todo_list.append(task)
        elif choice == '2':
            try:
                task_index = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_index < len(todo_list):
                    todo_list.pop(task_index)
                else:
                    print("\033[1;31mInvalid task number!\033[0m")
            except ValueError:
                print("\033[1;31mPlease enter a valid number!\033[0m")
        elif choice == '3':
            print("\033[1;32mGoodbye!\033[0m")
            break
        else:
            print("\033[1;31mInvalid choice, please try again.\033[0m")

if __name__ == "__main__":
    main()
