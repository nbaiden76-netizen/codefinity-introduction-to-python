# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

#checkout = [2.99, 5.49, 3.99]
#total = sum(checkout)
#print(total)  

#freezer_temperatures = [38, 32, 41, 34, 40]
#print(max(freezer_temperatures))  
#print(min(freezer_temperatures))


#price1 = "3.99"
#price2 = 12

# Convert prices to float
#price1_converted = float(price1)
#price2_converted = float(price2)

#print(f"Price #1 is ${price1_converted} and is of type {type(price1_converted)}")
#print(f"Price #2 is ${price2_converted} and is of type {type(price2_converted)}")

#price = 3.99
#quantity = "4"

# Calculate the total cost
#total_cost = int(quantity) * price

#print(f"The total cost for {quantity} items is ${total_cost}")
#print(f"Converting the total cost to an integer results in ${int(total_cost)}")

#fruit_prices = {"cherries": 3.99, "apples": 2.99, "bananas": 1.49}

# Sorting the dictionary keys alphabetically
#sorted_prices = sorted(fruit_prices)

#print(sorted_prices)

#products = ["apple", "banana", "cherry"]
#prices = [0.99, 0.59, 2.99]
#stock = [50, 100, 25]

# `zip()` combines the 3 lists into a series of tuples
# `list()` converts the zip object into a list
#product_info = list(zip(products, prices, stock))

#print("Product information:", product_info)

for product, values in products.items():
    price = float(values[0])
    qty = int(values[1])
    total = price * qty
    
    total_sales_list.append(total)
    print(f"Total sales for {product}:${total}")
    
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)


print(f"\nTotal sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")
      
    