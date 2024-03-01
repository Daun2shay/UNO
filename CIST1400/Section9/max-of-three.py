num1 = int(input())
num2 = int(input())
num3 = int(input())
max_value = max(num1, num2, num3)
    

if num1 == num2 == num3:
    print(f"Max of [{num1}, {num2}, {num3}] is {max_value} (all equal)")
else:
    print(f"Max of [{num1}, {num2}, {num3}] is {max_value}")