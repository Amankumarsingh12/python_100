class User:
    val = 20

#always call when we initialise User
    def __init__(self, id, name, place, ) :
        self.id = id
        self.name = name
        self.place = place
        self.follower = 0
        self.following = 0
        print("i am called", self.name)

    def follow(self, user):
        self.follower += 1
        self.following += 1

user_1 = User(1, "aman", "patna")
user_2 = User(2, "kumar", "bhopal")

print("usser_1", user_1.id, user_1.name, user_1.place)

user_1.follow(user_2)

print(user_1.follower, user_1.following,  user_2.follower, user_2.following)
        