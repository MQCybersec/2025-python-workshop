from pwn import *

context.log_level = "debug"

p = process(["python", "guessing-auto.py"])

n = int("tulip", 36) * int("punda", 36) * int("tenzin", 36) * int("jahin", 36)

l = 0
u = n-1

res = None

while l <= u:
    guess = l + (u - l) // 2
    p.recvuntil(b"Guess! ")
    p.sendline(str(guess).encode())
    
    hint = p.recvline().decode().strip()
    
    if hint == "Higher!":
        l = guess + 1
    elif hint == "Lower!":
        u = guess - 1
    else:
        res = hint
        break

print(res)