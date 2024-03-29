import random

total_points = 0

for roundCount in range(1, 7):
    print("Round", roundCount)

    round_points = 0
    while (round_points < 21):
        roolA = random.randint(1, 6)
        roolB = random.randint(1, 6)
        roolC = random.randint(1, 6)

        print(f'yout rolled {roolA}, {roolB}, and {roolC}')

        if roolA == roolB == roolC == roundCount:
            print("You rolled a Bunko!")
            round_points += 21

        elif roolA == roolB == roolC:
            print("Mini Bunko")
            round_points += 5

        elif roolA == roundCount:
            round_points += 1
        elif roolB == roundCount:
            round_points += 1
        elif roolC == roundCount:
            round_points += 1
        if (roolA != roundCount) and (roolB != roundCount) and (roolC != roundCount):
            break
    total_points += round_points
    print("your total score is", total_points)
print("final score is", total_points)
