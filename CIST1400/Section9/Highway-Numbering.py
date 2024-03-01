def classify_highway(highway_number):

  
  if not isinstance(highway_number, int) or highway_number < 0 or highway_number > 999:
    return f"{highway_number} is not a valid interstate highway number."

 
  if 1 <= highway_number <= 99:
    direction = "north/south" if highway_number % 2 != 0 else "east/west"
    return f"I-{highway_number} is primary, going {direction}."


  if 100 <= highway_number <= 999 and 1 <= highway_number % 100 <= 99:
    primary_highway = highway_number % 100
    return f"I-{highway_number} is auxiliary, serving I-{primary_highway}."


  return f"{highway_number} is not a valid interstate highway number."


highway_number = int(input())


print(classify_highway(highway_number))
