from datetime import datetime

def days_between_dates(date1: str, date2: str) -> int:
    
    # To calculate the number of days between the two dates  
    
    # Converting the string dates to the datetime.date
    da1 = datetime.strptime(date1, "%d/%m/%Y").date()
    da2 = datetime.strptime(date2, "%d/%m/%Y").date()
    
    # Returning the absolute difference in days
    return abs((da2 - da1).days)

if __name__ == "__main__":
    # User input 
    date1 = input("Enter the first date (DD-MM-YYYY): ")
    date2 = input("Enter the second date (DD-MM-YYYY): ")
    
    
    # Result 
    days_difference = days_between_dates(date1, date2)
    print(f"The number of days between {date1} and {date2} is {days_difference} days.")
