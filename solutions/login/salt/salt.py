users = dict()

# Alice: hunter2
# Bob: pizza
# Carol: Jh7H5^$21#VVLQdF

with open("users.dat") as F:
    G = F.read().split("\n")
    for i in range(len(G)):
        lst = G[i].split(":")
        users[lst[0]] = list((bytes.fromhex(lst[1]), bytes.fromhex(lst[2])))

username = input("Username: ")
password = input("Password: ")

import os
from hashlib import sha256
from hmac import compare_digest

if ":" in username:
    print("No colons in username.")
    
elif username not in users:
    print("User not found. Adding user.")
    
    salt = os.urandom(16)
    digest = sha256(salt + password.encode()).digest().hex()
    
    with open("users.dat", "a") as f:
        f.write(f"\n{username}:{salt.hex()}:{digest}")

elif compare_digest(sha256(users[username][0] + password.encode()).digest(), users[username][1]):
    print(f"Welcome, {username}!")

else:
    print("Incorrect password.")