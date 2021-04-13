age = 27
print(f"You are {age}")

name = "Tiago"
final_greeting = "How are you, {}?"
tiago_greeting = final_greeting.format(name)
print(tiago_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

name = "Jerry"
final_greeting = "How are you, {}?"
print(final_greeting.format(name))