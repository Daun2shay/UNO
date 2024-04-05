def max_magnitude(user_val1, user_val2, user_val3):
    max_val = max(abs(user_val1), abs(user_val2), abs(user_val3))
    return max_val

# Main program
val1 = int(input())
val2 = int(input())
val3 = int(input())

if __name__ == '__main__':
    result = max_magnitude(val1, val2, val3)
    print(result)