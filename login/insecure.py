# INSECURE! How could we store the passwords instead?
users = {
    "Alice": "hunter2",
    "Carol": "Jh7H5^$21#VVLQdF",
    "Bob": "pizza"
}

username = input("Username: ")
password = input("Password: ")

if username not in users:
    print("User not found.")
# Do we need to change anything here?
# hmac.compare_digest(b1, b2) provides an O(1) (constant time) string / bytes comparison function. You will have to import the hmac library
elif users[username] != password:
    print("Incorrect password.")
else:
    print(f"Welcome, {username}!")
