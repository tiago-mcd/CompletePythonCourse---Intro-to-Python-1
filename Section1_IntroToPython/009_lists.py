#lists - good way to organize variables
friends = ["Bruno", "Guilherme", "Rodrigo", "Vitor"]

print(friends[0]) #start counting im 0
print(friends)

#TIP: keep lists with one type of variable

print(len(friends)) #length of list

friends_ages = [
    ["Bruno", 26], 
    ["Guilherme", 28],
]

print(friends_ages[0])
print(friends_ages[1][1])

#add to list
friends.append("John")
print(friends)

#remove from list
friends.remove("John")
friends_ages.remove(["Guilherme", 28])

print(friends)
print(friends_ages)

#join lists
bros = ["Rolf", "Bruno", "Charles"]
comma_separated = ", ".join(bros)
print(f"My friends are {comma_separated}.")