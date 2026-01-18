prices = [29.99, 45.50, 12.75, 38.20]
discount_factor = [0.10, 0.20, 0.15,0.05]

# List of grocery items
# grocery_list = ["Apples", "Bananas", "Carrots", "Cucumbers"]

# Initialize a for loop to iterate over indexes
#for item in range(len(grocery_list)):
#    print("Index:", item)
#    print("Item:", grocery_list[item])
#    print("----")  # Printing a divider line for clarity

# List of original prices of grocery items
#prices = [1.50, 2.00, 0.75, 3.25]

# Discount factor (10% off each item)
#discount_factor = 0.10

# Iterate over the list of prices using range(len())
#for cost in range(len(prices)):
    # Apply the discount by reducing the price
#    prices[cost] -= prices[cost] * discount_factor
#    print(f"New price of item {cost + 1}: ${prices[cost]}")

#print("Updated prices:", prices)

for index in range(len(prices)):
    #attempt to apply the discount 
    prices[index]-= prices[index] * discount_factor[index]
    print(f"Updated price for item {index}: ${prices[index]:.2f}")