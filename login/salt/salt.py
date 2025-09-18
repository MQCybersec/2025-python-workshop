# A salt is a (normally random) string that is mixed in with the original data somehow before it is hashed. For example,
# a basic salted hash would be computed as such. Given a salt and a message,

# hash(salt || message)
 
# ...where || means concatenate. These are designed to protect against rainbow table attacks and
# to ensure uniqueness of each hash. For example, two users having the same password means that their
# password hashes will also be the same. Someone can then tell that these two users have the same password.

# If the passwords are salted (RANDOMLY) before hashing, two users with the same password will have COMPLETELY DIFFERENT hashes.

# You can embed the salt in your message however you want: as long as it is consistent. Prepend, append, or interleave

# STILL INSECURE! How could we also salt the hashes too! (Remember, the salt technically doesn't need to be secret!)
# You can use urandom(n) from the os library to generate cryptographically secure bytestreams
# os.urandom(16) generates 16 random bytes

# You've upscaled! You need to store and load your information in a file (users.dat) now! 
# It is up to you how you want to store the users and data in users.dat
# A suggested format could be something like username.salt.hash
users = None

username = input("Username: ")
password = input("Password: ")

# Users and their login details should be added to the users.dat file if they are not in it.

if username not in users:
    print("User not found.")
elif users[username] != password:
    print("Incorrect password.")
else:
    print(f"Welcome, {username}!")