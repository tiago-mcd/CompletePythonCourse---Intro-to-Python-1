#tuples store multiple types of informations like a list
#but are used when you want to keep things unchanged.
#use lists only when you want allow change.

short_tuple = "Bruno", "Guilherme"
#use this notation
a_bit_clearer = ("Bruno", "Guilherme")
tuple_in_list = [("Bruno", "Guilherme")]
is_a_tuple = "Bruno",
not_a_tuple = "Bruno"

#cannot .append
friends = "Bruno", "Guilherme"
friends = friends + ("Rodrigo",)