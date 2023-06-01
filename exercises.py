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
