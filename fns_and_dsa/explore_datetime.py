from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after adding {days_to_add} days: {formatted_future_date}")
        return future_date
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None