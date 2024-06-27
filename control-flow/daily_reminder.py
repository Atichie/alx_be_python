# Prompt for a Single Task
task = input("Enter your task: ")           
priority = input("Priority (high/medium/low): ")                           
time_bound = input("Is it time-bound? (yes/no): ").lower()        
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match priority: 
    case "high":
        if time_bound == "yes":
            print(f"Reminder: The task '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: The task '{task}' does not require immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: The task '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: The task '{task}' does not require immediate attention today!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: The task '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: The task '{task}' does not require immediate attention today!")
                                                                                       
                   
                                                              
               
                                                           
            
                                                                 
                       
                                                           
                                    
      
                                                                   
                                                              
