# with open("text.txt") as file:
#     content = file.read()
#     print(content)

with open("text.txt", mode="a") as file:
    file.write('\nNew line')