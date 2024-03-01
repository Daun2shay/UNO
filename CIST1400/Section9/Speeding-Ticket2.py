def calculate_ticket(speed_limit, driving_speed):
    ticket_amount = 0

    if driving_speed <= speed_limit - 10:
        ticket_amount = 50
    elif speed_limit + 6 <= driving_speed <= speed_limit + 20:
        ticket_amount = 75
    elif speed_limit + 21 <= driving_speed <= speed_limit + 40:
        ticket_amount = 150
    elif driving_speed > speed_limit + 40:
        ticket_amount = 300

    return ticket_amount


speed_limit = int(input())
driving_speed = int(input())

ticket_amount = calculate_ticket(speed_limit, driving_speed)
print(ticket_amount)