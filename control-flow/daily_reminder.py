# Prompt for a Single Task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").strip()
time_bound = input("Is the task time-bound? (yes/no): ").strip()  
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match priority: 
    case "high":
        reminder = f"The task '{task}' is of high priority" 
    case "medium":
        reminder = f"The task '{task}' is of medium priority" 
    case "low":
        reminder = f"The task '{task}' is of low priority."
    case _:
        reminder = f"The task '{task}' has unspecified priority."
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    reminder += " Consider completing it when you have free time." 
    print(f"Reminder: {reminder}")                            
