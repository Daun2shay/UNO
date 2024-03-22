def count_characters(text):
    count = 0
    for char in text:
        if char not in [' ', '.', '!', ',']:
            count += 1
    return count

input_text = input("Enter a line of text: ")
result = count_characters(input_text)
print(result)