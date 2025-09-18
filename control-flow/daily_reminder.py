# daily_reminder.py
def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")
    
    priority = priority.lower().strip()
    time_bound = time_bound.lower().strip()
    
    reminder = ""
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' is a task"
    
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += "."
    
    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()
