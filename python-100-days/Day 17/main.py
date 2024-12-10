class User:
    def __init__(self, user_id, name):
        self.id = user_id,
        self.name = name
        self.followers = 0
        self.folowing = 0

    def follow(self, user):
        user.followers += 1
        self.folowing += 1


user_1 = User(1, "kokush")
user_2 = User(2, "test")

user_2.follow(user_1)