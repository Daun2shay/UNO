# Get the number of integers
num_integers = int(input())

# Get the integers
integers = []
for _ in range(num_integers):
    integer = int(input())
    integers.append(integer)

# Get the threshold
threshold = int(input())

# Output the integers less than or equal to the threshold
output = ""
for integer in integers:
    if integer <= threshold:
        output += str(integer) + ","

print(output)