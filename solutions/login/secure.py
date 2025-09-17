# SHA256
users = {
    "Alice": "f52fbd32b2b3b86ff88ef6c490628285f482af15ddcb29541f94bcf526a3f6c7", # hunter2
    "Carol": "9b71d6ffe266d98638ecac62bce2c5c764ebe7fe9dc9d48e065f6a67fae92758", # Jh7H5^$21#VVLQdF
    "Bob": "9ed1515819dec61fd361d5fdabb57f41ecce1a5fe1fe263b98c0d6943b9b232e" # pizza
}

username = input("Username: ")
password = input("Password: ")

from hmac import compare_digest
import hashlib

if username not in users:
    print("User not found.")
elif compare_digest(hashlib.sha256(password.encode().digest(), bytes.fromhex(users[username]))):
    print(f"Welcome, {username}!")
else:
    print("Incorrect password.")
