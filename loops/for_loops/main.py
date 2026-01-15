prices = [12.99, 8.50, 15.75, 23.00, 7.25]

# Write your code here

# groceryItems = ["milk", "eggs", "cheese", "butter"]
# for item in groceryItems:
    # Code to be executed
   # print(item)

# Dictionary of products and their stock counts
# productStock = {"milk": 120, "eggs": 200, "bread": 80}

# Print each dictionary key
# print("Product list:")
# for product in productStock:
  #   print(product)

# Dictionary of products and their stock counts
#productStock = {"milk": 120, "eggs": 200, "bread": 80}

# Print both the key and value for each dictionary item
#print("Inventory details:")
#for product, stock in productStock.items():
   # print(f"{product} has {stock} units in stock.")

# Product names as keys and their stock levels as values
#inventory = {
 #   "milk": 120,
 #   "eggs": 30,
  #  "bread": 80,
  #  "apples": 10
#}

# The threshold stock level that triggers a restock
# minimum_stock = 50

# Evaluating stock levels and deciding if restocking is necessary
# print("Checking inventory status:")
# for product, quantity in inventory.items():
#    if quantity < minimum_stock:
 #       print(f"{product} requires restocking. Only {quantity} units remain.")
 #   else:
 #       print(f"{product} has adequate stock with {quantity} units available.")

# Task 
total = 0 
for item in prices:
    total = total + item
    print(total)
