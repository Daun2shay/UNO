# Read the number of values
num_values = int(input())

# Read the values
values = []
for _ in range(num_values):
    value = float(input())
    values.append(value)

# Find the largest value
max_value = max(values)

# Adjust and print the values
for value in values:
    adjusted_value = value / max_value
    print(f'{adjusted_value:.2f}')