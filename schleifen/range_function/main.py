# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Initialize the `for` loop to iterate over the range of indices using `range()` function
for day in range(5): 
    weekday = weekdays[day]  # Get the current weekday
    promotion = daily_promotions[day]  # Get the promotion for the current day
    print(f"{weekday}: Promotion on {promotion}")