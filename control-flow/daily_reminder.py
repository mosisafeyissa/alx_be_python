def daily_reminder():
    # Get user input
    task = input("Enter your task: ").strip()
    while not task:
        task = input("Task cannot be empty. Enter your task: ").strip()
    
    priority = input("Priority (high/medium/low): ").strip().lower()
    while priority not in ['high', 'medium', 'low']:
        priority = input("Invalid priority. Enter high/medium/low: ").strip().lower()
    
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    while time_bound not in ['yes', 'no']:
        time_bound = input("Please answer yes/no: ").strip().lower()

    # Process and display reminder
    urgency = "that requires immediate attention today!" if time_bound == 'yes' else ""
    
    match priority:
        case 'high':
            print(f"Reminder: '{task}' is a high priority task {urgency}")
        case 'medium':
            print(f"Note: '{task}' is a medium priority task {'to complete today.' if urgency else 'for this week.'}")
        case 'low':
            print(f"Note: '{task}' is a low priority task {'with a deadline.' if urgency else 'for free time.'}")

if name == "main":
    daily_reminder()
