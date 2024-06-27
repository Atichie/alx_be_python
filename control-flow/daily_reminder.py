# Prompt for a Single Task
Task = input("Enter your task: ")
Priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time_bound? (yes/no): ")
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match Priority: 
    case "high":
        reminder = f"The task '{Task}' is of high priority."
    case "medium":
        reminder = f"The task '{Task}' is of medium priority."
    case "low":
        reminder = f"The task '{Task}' is of low priority."
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
    print(reminder)
else:
    reminder += " Consider completing it when you have free time." 
    print(reminder)                                           
