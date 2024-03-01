def is_leap_year(year):

  if year % 400 == 0:
    return True
  elif year % 100 == 0:
    return False
  else:
    return year % 4 == 0

# Get user input
year = int(input())

# Check if it's a leap year and print the result
if is_leap_year(year):
  print(f"{year} - leap year")
else:
  print(f"{year} - not a leap year")
