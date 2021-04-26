#dictionaries
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])

friend_ages["Bob"] = 26 #add new key/value
friend_ages["Rolf"] = 25 #change value for a key

friends = (  #tupple dictionary
    {"name": "Rolf Smith", "age": 24},
    {"name": "Jonh Smith", "age": 82},
    {"name": "Charles Kingsley", "age": 29}
)

print(friends[0]["name"])

friend = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend = dict(friend) #convert list in dictionary
print(friend)