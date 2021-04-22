#sets are another collection of data like lists and tuples.
#the key difference is sets don't hold order and don't 
#contain duplicates. usefull for comparisson.

art_friends = {"Bruno", "Guilherme"}
science_friends = {"Rodrigo", "Vitor"}

art_friends.add("Rodrigo") #add anywhere in art_friends
print(art_friends)

art_friends.add("Rodrigo") #doesn't add again
print(art_friends)

art_friends.remove("Rodrigo")
print(art_friends)

#advanced sets operations
humans = {"Rolf", "Anne", "Jen"}
aliens = {"Jen", "Charlie"}

humans_not_aliens = humans.difference(aliens)
aliens_not_aliens = aliens.difference(humans)

print(humans_not_aliens)
print(aliens_not_aliens)

not_in_both = humans.symmetric_difference(aliens)
print(not_in_both)

aliens_humans = aliens.intersection(humans)
print(aliens_humans)

all_beings = humans.union(aliens) #no duplicates
print(all_beings)