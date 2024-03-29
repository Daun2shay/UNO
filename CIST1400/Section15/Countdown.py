def countdown(num):
    # Check if the input is within the valid range
    if num < 11 or num > 99:
        print("Input must be 11-99")
        return

    # Start the countdown
    while True:
        print(num)
        # Check if both digits are identical
        if num // 10 == num % 10:
            break
        num -= 1

# Get user input
num = int(input())

# Call the countdown function
countdown(num)