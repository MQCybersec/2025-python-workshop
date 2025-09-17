from random import randint
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import base64
from hashlib import sha256
from pwn import *

# context.log_level = "debug"

server = process(["python", "receiver.py"])

p_line = server.recvline().decode().strip().split()[-1]
g_line = server.recvline().decode().strip().split()[-1]

p = int(p_line, 16)
g = int(g_line)

y = randint(2, p-2)
gy = pow(g, y, p)

server.recvuntil(b"Your g^y mod p (in HEX): ")
server.sendline(hex(gy)[2:].encode())

gx_line = server.recvline().decode().strip().split()[-1]
gx = int(gx_line, 16)

shared_int = pow(gx, y, p)

key = sha256(long_to_bytes(shared_int)).digest()

iv_line = server.recvline().decode().strip().split()[-1]
cipher_line = server.recvline().decode().strip().split()[-1]

iv = base64.b64decode(iv_line)
cipher = base64.b64decode(cipher_line)

aes = AES.new(key, AES.MODE_CBC, iv=iv)
message = aes.decrypt(cipher)

server.recvuntil(b"What was my original message? ")
server.sendline(message)

res = server.recvline().decode().strip()
print(res)