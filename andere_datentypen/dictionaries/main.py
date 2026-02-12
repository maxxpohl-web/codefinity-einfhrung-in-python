# Dictionary erstellt 
grocery_inventory = {"Milk" : (113, "Diary"), "Eggs" : (116, "Dairy"), "Bread" : (117, "Bakery"), "Apples" : (141, "Produce") }
# Diargramm {key : (tuple) , key : (tuple) }

bread_details = grocery_inventory["Bread"]
print(bread_details)

print("Bread : Details of Bread:" , bread_details)

grocery_inventory.update({"Cookies" : (143, "Bakery")})

print("Inventory after adding Cookies: " , grocery_inventory)

grocery_inventory.pop("Eggs")

print("Inventory after removing Eggs: " , grocery_inventory)




