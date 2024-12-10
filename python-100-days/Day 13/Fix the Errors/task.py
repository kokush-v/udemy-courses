try:
    age = int(input("How old are you?"))
except ValueError:
    print('You can use only numbers')
    age = int(input("How old are you?"))


if age > 18:
    print(f"You can drive at age {age}.")
