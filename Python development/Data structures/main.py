#list operations
#creating a list
cars=["marcedes-Benz", "Range rover", "Audi A4", "Subaru"]
print(cars)
#length of the list-number of items
print(f"Lenght of list:{len(cars)}")
#access the elements in a list
print("The second element is:", cars[1])
#adding an element
cars.append("BMW 3 series")
print("added BMW 3 series", cars)
#removing an item
cars.remove("Subaru")
print("Removed Subaru:", cars)
#sort the list
cars.sort()
print("Sorted list:", cars)