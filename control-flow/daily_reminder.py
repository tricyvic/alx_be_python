task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
        else:
            print("please choose 'yes' if time-bound is high or 'no'if timebound is low")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print("please choose 'yes' if time-bound is high or 'no'if timebound is low")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print("please choose 'yes' if time-bound is high or 'no'if timebound is low")
    case _:
        print("please choose between 'high',medium or 'low' please")

