# As a senior backend engineer,
# you are tasked with developing a fast in-memory data structure to manage profile information
# (username, name and email) for 100 million users.
# It should allow the following operations to be performed efficiently:

# Insert the profile information for a new user.
# Find the profile information of a user, given their username
# Update the profile information of a user, given their usrname
# List all the users of the platform, sorted by username
# You can assume that usernames are unique.

# simple solution
class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def list_all(self):
        return self.users

# Insert = O(N)
# Find = O(N)
# Update = O(N)
# List = O(1)