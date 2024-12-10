import  random

# 1 option
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0, len(friends) - 1)

print(f"{friends[random_index]} will pay today")

# 2 option
print(f"{random.choice(friends)} will pay today")