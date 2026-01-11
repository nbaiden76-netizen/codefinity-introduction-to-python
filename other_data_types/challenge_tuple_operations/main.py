# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
# going to use a tupe to count how many apples appear in the "shelf" tupe
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)
# Now to index the first occurance of the shelf tupe "bananas 
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)
# checking the number of apples is less than 5 in a if statement
if apple_count < 5:
	print("Apples need to be restocked.")
else:
	print("Apples are sufficently stocked.")
# Now to count how many times that "grapes" appers in the shelf tupe
grape_count = shelf.count("grapes")
# Now another if statement to see if there is any grapes in the shelf tupe
if grape_count == 1:
	print("Grapes need to be restocked.")
else:
	print("Grapes are sufficiently stocked")
# Now to check whether Oranges are in stock or not

orange_index = shelf.index("oranges")
# Now an if statement to see if we have any in stock
if "oranges" in shelf:
	print("Oranges are at Index:", orange_index)
else:
	print("Oranges are out of stock.")
	









