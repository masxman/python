import datetime
today = datetime.datetime.now().date()
print("current date is",today)
days_to_add = int(input("Enter the number of days to add : "))
new_date=today + datetime.timedelta(days=days_to_add)
print("date after adding",days_to_add, " days is :", new_date)
