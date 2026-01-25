# List of product prices
#product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
#updated_prices = apply_discount(product_prices)

#def add_strawberry(original_list):
 #   list_copy = original_list.copy()  # Create a copy of the original list
#    list_copy.append("Strawberry")  # Modify the copied list
 #   return list_copy

# Original list
#fruits = ["Apple", "Banana", "Cherry"]

# Call the function
#new_fruits = add_strawberry(fruits)

# Check the results
#print("Original list:", fruits)   # ['Apple', 'Banana', 'Cherry']
#print("Modified list:", new_fruits)  # ['Apple', 'Banana', 'Cherry', 'Strawberry']

# Now for the Task 
def apply_discount(prices):
    prices_copy = prices.copy() # creates a copy of the prices list 
# now  a 'For ' loop 
    for index in range(len(prices_copy)):
        if prices_copy[index] > 2.00:
            prices_copy[index] *= 0.90 
    return prices_copy

# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print("Updated product prices:", updated_prices)

