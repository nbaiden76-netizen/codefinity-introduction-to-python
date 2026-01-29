# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold


# defining the Calculated revenue 
def calculate_revenue(prices,quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

calculate_revenue(prices, quantities_sold)

revenue = calculate_revenue(prices, quantities_sold)

# defining the formated output 
def formatted_output(pairs):
    for product, revenue in pairs:
# Example of expected output line (do not remove):
        print(f"{product} has total revenue of ${revenue}")



revenue_per_product  = list(zip(products, revenue))


sorted_revenue_products = sorted(revenue_per_product)
formatted_output(sorted_revenue_products)
