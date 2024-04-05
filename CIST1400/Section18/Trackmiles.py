def laps_to_miles(user_laps):
    miles = user_laps * 0.25
    return miles

if __name__ == '__main__':
    user_laps = float(input())
    miles = laps_to_miles(user_laps)
    print(f'{miles:.2f}')