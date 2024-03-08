def reverse_binary(n):
    result = ""
    while n > 0:
        result += str(n % 2)
        n //= 2
    return result

# Test the function
num = int(input("Enter a positive integer: "))
print(reverse_binary(num)) 