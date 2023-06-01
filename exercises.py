print("")
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
print("______________________________________________________________________")
print("")

print("Exercise two: tupple with seven items useing while loop")

# Create and print tuple
videoGames = ("Super Mario Bros", "Valorant", "Minecraft", "CSGO", "Grand Theft Auto V", "Overwatch", "Fortnite")
index = 0
print("The video games in the tuple are: ", videoGames)
print("")
print("")

# Now useing while loop
print("Video game titles using a while loop:")
while index < len(videoGames):
    gameTitle = videoGames[index]
    print(f"Game at index {index}: {gameTitle}")
    index += 1

print("")
print("______________________________________________________________________")
print("")

print("Exercise three: Modify a dictionary")
print("")
print("")

# We create dictionary
dictionary = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Current dictionary:", dictionary)
print("")
print("")

# Now we modify the dictionary
print("Please modify one of the next properties(name, age, or city)")
propertyName = input("Enter the name of the property to modify: ")
print("")

if propertyName in dictionary:
    newValue = input("Enter the new value: ")
    dictionary[propertyName] = newValue
    print("")
    print("Modified dictionary:", dictionary)

# If we dont enter a valid property it will pop an error
else:
    print("")
    print("Error: Property not found in the dictionary.")

print("")
print("______________________________________________________________________")
print("")

print("Exercise four: create a function named operation, that receives 3 parameters")
print("")
print("")

# First we define the needed for the operation
def operation(numberOne, operand, numberTwo):
    if operand == '+':
        result = numberOne + numberTwo
    elif operand == '-':
        result = numberOne - numberTwo
    elif operand == '*':
        result = numberOne * numberTwo
    elif operand == '/':
        if numberTwo != 0:
            result = numberOne / numberTwo
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Error: Invalid operand.")
        return None
    return result


# Perform operation
# First we input the 3 parameters as indicated
numberOne = int(input("Enter the first number: "))
print("")
operand = input("Enter the operand (+, -, *, /): ")
print("")
numberTwo = int(input("Enter the second number: "))
print("")
print("")

# Then we show the results
result = operation(numberOne, operand, numberTwo)
if result is not None:
    print("Result:", result)

print("")
print("______________________________________________________________________")
