# Prompt for a Single Task
Task = input("Enter your task: ")
Priority = input("Priority(high/medium/low): ").strip().lower()
Time_Bound = input("Is it time_bound? (yes/no): ").strip().lower()
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match Priority: 
    case "high":
        reminder = f"The task '{Task}' is of high priority" 
    case "medium":
        reminder = f"The task '{Task}' is of medium priority" 
    case "low":
        reminder = f"The task '{Task}' is of low priority."
    case _:
        reminder = f"The task '{Task}' has unspecified priority."
if Time_Bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    reminder += " Consider completing it when you have free time." 
    print(f"Reminder: {reminder}")                            
