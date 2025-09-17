from pwn import *

# comment this line out if you don't want to see a bunch of text
context.log_level = "debug"

# If you were communicating with a real server, you'd use these
# HOST = "host"
# PORT = 1337
# p = remote(HOST, PORT)

p = process(["python", "guessing-auto.py"])

# a // b is the same as floor(a / b) in Python (Integer division)