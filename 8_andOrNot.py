age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age < 150

print(f"You can learn programming: {can_learn_programming}.")

new_age = int(input("Enter your age: "))
usually_working = age >= 18 or age <= 65
print(f"At {new_age} you are usually working!")

x = 35 and 0
y = 0 or 35

print(bool(x))
print(bool(y))

name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}"
print(f"Hello, {greeting}!")

#not invert the boolean value
print(not False)
print(not True)