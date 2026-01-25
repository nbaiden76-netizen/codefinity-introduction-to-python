# Call the (function and print the result
#apples_total_cost = calculate_total_cost(1.50, 10)

# parameters and arguments 

#def greet_customer(name):
#    print(f"Hello, {name}! Welcome to our store.")

#greet_customer("Alice")

# in the example above 'name' is the paramenter, and string "Alice" is the argument 

# Function to check stock levels of grocery items
# ...
# def check_stock(inventory):
#    for item, stock in inventory.items():
#        if stock < 10:
#            print(f"Warning: {item} is running low on stock with only {stock} units left!")
#            print("Please restock the item before proceeding with the check.")
 #           return  # Stops the function if stock is below 10
#        print(f"{item} has sufficient stock: {stock} units.")
    
#    print("All items have sufficient stock.")

# Example inventory of a grocery store
#inventory = {
#    "Apples": 50,
 #   "Bananas": 30,
#    "Milk": 8,  # This will trigger the early exit
#    "Bread": 25
#}

# Check stock levels
#check_stock(inventory)

# `cost` and `discount_rate` are the parameters of the function
#def calculate_discounted_price(cost, discount_rate):
 #   final_price = cost * (1 - discount_rate)
  #  return final_price

# Call the `calculate_discounted_price` function and pass in `cost` and `discount_rate` values as arguments
#apples_final_price = calculate_discounted_price(1.2, 0.10)
#milk_final_price = calculate_discounted_price(2.2, 0.15)
#bread_final_price = calculate_discounted_price(0.8, 0.05)

# Display the discounted prices
#print(f"The discounted price of apples is ${apples_final_price}")
#print(f"The discounted price of milk is ${milk_final_price}")
#print(f"The discounted price of bread is ${bread_final_price}")

def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    return total_cost

# Call the function and print the result
apples_total_cost = calculate_total_cost(1.50, 10)
print(f"The total cost for apples is ${apples_total_cost}")