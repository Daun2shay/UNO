city_state_dict = {}

while True:
    city = input("Enter a city, 'quit' to end: ")
    if city == 'quit':
        break
    state = input("Enter a state: ")
    city_state_dict[city] = state
    if city == "No cities to list!":
        print("No cities to list!")
    else:
        print(f"Added {city}, {state} to dictionary!")

if len(city_state_dict) == 0:
    print("No cities to list!")
else:
    print(f"There are {len(city_state_dict)} cities in the dictionary: {city_state_dict}")