# working with attributes, class constructor and init

class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0 # Default attribute
        self.following = 0 # Default attribute

    def follow(self,user): # when a user decides to follow another user
        user.followers += 1
        self.following += 1


user1 = User("001", "Angela")
user2 = User("002", 'Jack')

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

# print(user1.id)
# print(user1.name)
# print(user1.followers)
# user1.id = '002'
# user1.username = 'Sayanti'
# print(user1.username)



