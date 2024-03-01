def calculate_movie_price(time_of_day, age):


  if age < 4:
    price = "free"
  elif time_of_day == "day":
    price = "$8"
  else:
    if age <= 16:
      price = "$12"
    elif age <= 54:
      price = "$15"
    else:
      price = "$13"
  return price


time_of_day = input().lower()
age = int(input())

price = calculate_movie_price(time_of_day, age)
print(f"{price}")