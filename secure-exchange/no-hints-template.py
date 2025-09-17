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
# p = remote(HOST, PORT)

p = process(["python", "receiver.py"])