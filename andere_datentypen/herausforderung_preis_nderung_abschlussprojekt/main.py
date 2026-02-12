#Dictionary anlegen 
grocery_inventory = {"Milk" : ("Dairy" , 3.50 , 8), 
                     "Eggs" : ("Dairy" , 5.50 , 30),
                     "Bread" : ("Bakery" , 2.99 , 15),
                     "Apples" : ("Produce" , 1.50 , 50)     
                    }

#print(grocery_inventory.get("Eggs")    #Abrufen was die Eier kosten 
eggs_price = grocery_inventory["Eggs"][1]



if eggs_price > 5: 
   grocery_inventory.update({"Eggs": ("Dairy", 4.50, 8)}) 
   print("Eggs are too expensive, reducing the price by $1. ")
else:
   print("The price of Eggs is reasonable.")

grocery_inventory.update({"Tomatoes" : ("Produce" , 1.20 , 30)})
print("Inventory after adding Tomatoes: ", grocery_inventory)

milk_units = grocery_inventory["Milk"][2]

if milk_units < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory.update({"Milk" : ("Dairy" , 3.50 , 28)})

else:
    print("Milk has sufficient stock.")

apple_price = grocery_inventory["Apples"][1]

if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:", grocery_inventory)








