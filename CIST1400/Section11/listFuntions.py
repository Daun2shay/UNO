
numbers = []
for i in range(4):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

sum_of_numbers = sum(numbers)

if sum_of_numbers > 20:
    
    minimum = min(numbers)
    print(f"Minimum: {minimum}")
else:
    
    maximum = max(numbers)
    print(f"Maximum: {maximum}")