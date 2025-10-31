# 100 Days of Python
# Day 17 - The advantages of OOP and Classes
# Creating a User class to demonstrate OOP concepts

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# Create two instances of User
user_1 = User("001", "Angela") 
user_2 = User("002", "Jack")

# Make user_1 follow user_2
user_1.follow(user_2)

# Print out the followers and following counts for both users
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
