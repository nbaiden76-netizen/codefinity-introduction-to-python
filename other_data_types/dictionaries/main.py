# A dictionary with various types of keys and values
# store_info = {
  #  "Store Name": "Grocery Galore",    # String key and string value
   # 42: "Inventory Count",             # Integer key and string value
   # ("Bread", "Milk"): [2.99, 1.59]    # Tuple key and list value (prices of bread and milk)
#}

# Extracting dictionary element (list) by its key (tuple)
#print("Data under key ('Bread', 'Milk'):", store_info[("Bread", "Milk")])


# Dictionary for a grocery store inventory
# inventory = {
 #   "Apples": 30,
  #  "Oranges": 18,
   # "Bananas": 45
#}

# Get the count of Oranges
# print("Count of Oranges:", inventory.get("Oranges"))

# Update inventory by adding a new item
# inventory.update({"Mangoes": 20})
# print("Updated Inventory:", inventory)

# You can also add a new item to the end of the dictionary like this
# inventory["Pineapples"] = 15
#print("Updated Inventory:", inventory)

# Remove Bananas from the inventory
#removed_item = inventory.pop("Bananas")
# print("Removed Item:", removed_item)
# print("Current Inventory:", inventory)

# Task foir Data Dictionaries - thinks got a little more complicated 

grocery_inventory = {"Milk": (113, "Dairy"), "Eggs": (116, "Dairy"), "Bread": (117, "Bakery"), "Apples": (141, "Produce ")}
# Now to retrive the details from Bread 
bread_details = grocery_inventory["Bread"]
print("Details of Bread:", bread_details)
# Adding a new item using the Data dictionary method "update" 
grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)
# removing an item from the list 
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)

