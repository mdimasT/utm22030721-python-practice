print("______________________________________________________________________")
print("")

print("Exercise one: add a number to the list")

# Create list
list = [1, 2, 3, 4, 5]
print(list)
print("")
print("")

# We add a number
addNumber = int(input("Please enter a new element for the list: "))
list.append(addNumber)
print("")

# And print the results
print("List elements using for loop:")
for item in list:
    print(item)

print("")
