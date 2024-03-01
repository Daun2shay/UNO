def change_calculator(amount):
  """Calculates the fewest coins needed to make change for a given amount.

  Args:
    amount: An integer representing the total change amount in cents.

  Returns:
    A string listing the coin denominations and their quantities, or "No change" if the amount is zero or negative.
  """

  # Define coin denominations and their values in cents.
  coins = {
      "Dollar": 100,
      "Quarter": 25,
      "Dime": 10,
      "Nickel": 5,
      "Penny": 1
  }

  # Initialize a dictionary to store the number of coins of each denomination.
  coin_counts = {coin: 0 for coin in coins}

  # If the amount is zero or negative, return "No change".
  if amount <= 0:
    return "No change"

  # Iterate through the coin denominations in descending order.
  for coin, value in coins.items():
    # Calculate the maximum number of coins of the current denomination that can be used.
    coin_count = amount // value
    # Update the amount remaining and the coin count dictionary.
    amount -= coin_count * value
    coin_counts[coin] = coin_count

  # Build the output string.
  output = ""
  for coin, count in coin_counts.items():
    if count > 0:
      # Use singular or plural coin name depending on the count.
      coin_name = coin + ("s" if count > 1 else "")
      output += f"{count} {coin_name}\n"

  return output.strip()

# Get user input for the amount
amount = int(input())

# Print the change breakdown
print(change_calculator(amount))