
numbers = []
while True:
    num = int(input())
    if num > 0:
        numbers.append(num)
    else:
        break

smallest = min(numbers)
largest = max(numbers)


print(f"{smallest} and {largest}")