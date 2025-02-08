# Ray McMillin, 2/7/25, Hot Dogs

def calculate_total_cost():
  tax_rate, hot_dog_price, chili_dog_price, cheese_price, peppers_price, grilled_onions_price = 0.07, 3.50, 4.50, 0.50, 0.75, 1.00

  print("Choose your hot dog:\n1. Hot Dog - $3.50\n2. Chili Dog - $4.50")
  hot_dog_pick = input('Reply with either "Normal", or "Chili":')

  if hot_dog_pick == "Normal": 
    price = hot_dog_price
  elif hot_dog_pick == "Chili":
    price = chili_dog_price
  else:
    print('That is not available. Please choose either "Normal", or "Chili".')
    return

  cheese = input("Would you like to add cheese for $0.50? 'YES or NO'")
  peppers = input("Would you like to add peppers for $0.75? 'YES or NO'")
  grilled_onions = input ("Would you like to add grilled onions for $1.00? 'YES or NO'")

  final_price = price
  if cheese == "YES" or cheese == "yes" or cheese == "Yes":
      final_price += cheese_price
  if peppers == "YES" or peppers == "yes" or peppers == "Yes":
      final_price += peppers_price
  if grilled_onions == "YES" or grilled_onions == "yes" or grilled_onions == "Yes":
      final_price += grilled_onions_price

  tax = final_price * tax_rate
  total = tax + final_price

  print(f"Hot Dog Cost: ${price:.2f}")
  print(f"Final Price (before tax): ${final_price:.2f}")
  print(f"Tax: ${tax:.2f}")
  print(f"Total Cost: ${total:.2f}")

calculate_total_cost()
