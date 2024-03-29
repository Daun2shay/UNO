# Get user input for triangle character
triangle_char = input('Enter a character:\n')
# Get user input for triangle height
triangle_height = int(input('Enter triangle height:'))
# Print
print('')

i = 0;

while i <= triangle_height :
    # Triangle character times i
    print(f'{triangle_char} '*i)
    i += 1