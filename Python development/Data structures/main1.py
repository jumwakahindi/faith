
#operations in a dictionary
electronics = {"computers": ["LED", "Cathode Ray Tube", "Super computer"]}
print(electronics)
#insert an item and value to the dictionary
electronics["main frame"] = "LED"
print(electronics)
#remove an item
electronics["computers"].pop(1)  # removes "Cathode Ray Tube"
print(electronics)
#access an item
print("computer example:", electronics["computers"][1])
#change the values
electronics["computers"][0] = "mini computer"
print(electronics)