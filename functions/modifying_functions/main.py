# Dictionary representing the current stock of products
inventory = {
    "apples": 17,
    "bananas": 75,
    "oranges": 2,
    "grapes": 50
}

# Function to restock items that have low stock levels by adding a specified amount
# def restock(product, inventory, restock_amount):
 #   inventory[product] += restock_amount
  #  print(f"Restock order placed for {product}. New stock level: {inventory[product]} units.")

# Function to check which items are below the stock threshold and trigger the `restock` function
#def check_stock_levels(inventory, threshold):
 #   for product, quantity in inventory.items():
  #      if quantity < threshold:
            # If the stock is below the threshold, call the `restock` function to add 50 units
   #         restock(product, inventory, 50)

## Checking the stock levels for all products in the inventory with a threshold of 30 units
#check_stock_levels(inventory, 30)

# Display the final inventory after restocking
#print("Final inventory status:", inventory)


# Define a function with a default `discount` argument
#def apply_discount(price, discount=0.10):
   # discounted_price = price * (1 - discount)
 #   return discounted_price

# Call the function without providing a `discount`, using the default value
#default_discount_price = apply_discount(100)
#print(f"Price after applying the default discount: ${default_discount_price}")

# Call the function with a custom `discount` value
#custom_discount_price = apply_discount(100, 0.20)
#print(f"Price after applying a custom discount: ${custom_discount_price}")

# Function where `tax` has a default value
#def calculate_total(price, discount, tax=0.05):
  #  total = price * (1 + tax) * (1 - discount)
  #  return total

# Calling the function using keyword arguments
#total_cost = calculate_total(price=100, discount=0.15)
#print(f"Total cost after applying discount: ${total_cost}")

# task: First define the discounted price 

def apply_discount(price, discount=0.05):
    price *= (1 - discount)
    return price

def apply_tax(price, tax=0.07):
    price *= (1 + tax)
    return price 

def calculate_total(price, discount=0.05, tax=0.07):
    discounted = apply_discount(price, discount)
    final = apply_tax(discounted, tax)
    return final

default_discount_price = calculate_total(120)
additional_discounted_price = calculate_total(100,discount=0.10, tax=0.08)

print(f"Total cost with default discount and tax: ${default_discount_price}")
print(f"Total cost with custom discount and tax: ${additional_discounted_price}")
