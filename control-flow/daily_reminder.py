# daily_reminder.py
def main():
    task = input("Enter your task: ").strip()
    priority = input("Enter priority (high, medium, low): ").lower().strip()
    time_bound = input("Is the task time-bound? (yes/no): ").lower().strip()
    
    reminder = ""
    match priority:
        case "high":
            reminder = f"High priority task: {task}"
        case "medium":
            reminder = f"Medium priority task: {task}"
        case "low":
            reminder = f"Low priority task: {task}"
        case _:
            reminder = f"Task: {task} (priority not specified)"
    
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += "."
    
    print(f"\nReminder: {reminder}")

if __name__ == "__main__":
    main()
