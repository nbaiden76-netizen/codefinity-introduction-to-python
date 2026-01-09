
vegetables = ["tomatoes", "potatoes", "onions"]
# removing onions from the list 
vegetables.remove("onions")
# If statement to ammend list 
if "carrots" in vegetables:
     print("Carrots are already in the list.")
else:
    vegetables.append("carrots")
    
if "cucumbers" in vegetables:
    print("Cucumber are already in the list.")
else:
    vegetables.append("cucumbers")
    
vegetables.sort()

print("Updated Vegetable Inventory:", vegetables)
