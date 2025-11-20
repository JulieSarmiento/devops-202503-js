
name = input("What's your name? ")
age = input("What's your age? ")

if (name and int(age) > 21):
    print(f"Hello, {name}! You are {age} years old, you are rich!")
else:
    print(f"Hello, {name}! You are {age} years old, you are a baby, so no money!")

