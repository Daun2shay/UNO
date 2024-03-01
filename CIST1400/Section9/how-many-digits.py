def count_digits(number):
 
  if number < 0 or number > 9999:
    raise ValueError()

  count = 0
  while number > 0:
    number //= 10
    count += 1

  return count

if __name__ == "__main__":
  try:
    number = int(input())
    num_digits = count_digits(number)
    print(f"{num_digits} digits")
  except ValueError as e:
    print(e)
