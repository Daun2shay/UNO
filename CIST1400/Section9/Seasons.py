months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

seasons = {
    "Spring": (3, 20, 6, 20),
    "Summer": (6, 21, 9, 21),
    "Autumn": (9, 22, 12, 20),
    "Winter": (12, 21, 3, 19)
}


def get_season(month_str, day):
    if month_str not in months or not 1 <= day <= 31:
        print("Invalid")
        return 

    month = months[month_str]
    for season, (start_month, start_day, end_month, end_day) in seasons.items():
     
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            print(season)
            return

    
        if start_month < end_month:
            if month > start_month and month < end_month:
                print(season)
                return
        else: 
            if month > start_month or month < end_month:
                print(season)
                return

    print("Invalid") 


month_str = input()
day = int(input())

get_season(month_str, day)