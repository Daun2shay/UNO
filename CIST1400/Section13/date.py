# Create the dictionary with month abbreviations and number of days
months = {
    'Jan': 31,
    'Feb': 28,
    'Mar': 31,
    'Apr': 30,
    'May': 31,
    'Jun': 30,
    'Jul': 31,
    'Aug': 31,
    'Sep': 30,
    'Oct': 31,
    'Nov': 30,
    'Dec': 31
}

# Output the dictionary
print(months)
print()

# Get user input
month = input("Enter 3 character abbreviation for month: ")
day = int(input("Enter day: "))
year = int(input("Enter year: "))

# Check if the date is valid
if month in months.keys() and 1 <= day <= months[month] and year >= 1752:
    # Check for leap year
    if month == 'Feb' and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        print(f"{month} {day}, {year} is a valid date.")
    elif month != 'Feb':
        print(f"{month} {day}, {year} is a valid date.")
    else:
        print(f"{month} {day}, {year} isn't a valid date.")
else:
    print(f"{month} {day}, {year} isn't a valid date.")