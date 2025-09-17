from random import randint
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import base64
from hashlib import sha256
from pwn import *

# comment this line out if you don't want to see a bunch of text
context.log_level = "debug"

# If you were communicating with a real server, you'd use these
# HOST = "host"
# PORT = 1337
# server = remote(HOST, PORT)

server = process(["python", "receiver.py"])

# 1. Receive the prime p and generator g. The prime p and will be in HEX, and the generator g will just be a decimal.
# You will have to convert p to an INTEGER from HEX, and g will be a string by default.


# 2. Generate a random integer y in the range [2, p-2], and compute g^y mod p. This can be done with the pow() function.
# 
# pow(a, b, c) will efficiently compute a^b (mod c).
#
# Convert g^y mod p it to hex and send it over to the server.

# The server will then send their g^x mod p (gx) to you in HEX. Receive this and store it as an INTEGER, then
# compute (g^x)^y mod p and store it in a variable (I will call it "shared_int"). Again, use the pow() function to do this.


# 3. Generate the shared key by first converting shared_int to BYTES (long_to_bytes() function from Crypto.Util.number can do this), 
# then hashing it with SHA256. This is now your shared key. Make sure this is a BYTES object.


# 4. The server has sent an IV and ciphertext encoded using Base64. Use this key and IV to construct a new AES object in CBC mode. 
# AES.new(key (bytes), AES.MODE_CBC, iv=iv (bytes)) constructs an AES object in CBC mode.

# 5. Decrypt the ciphertext given using the configuration and shared key, then send it back to the server. Receive the final string and print it.