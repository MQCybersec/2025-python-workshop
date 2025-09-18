from random import randint
# This library can be installed via the package name "pycryptodome"
# e.g. pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import base64
from hashlib import sha256
import os

# prime and generator from RFC 7919 
# https://datatracker.ietf.org/doc/html/rfc7919#page-19
p = 0xffffffffffffffffadf85458a2bb4a9aafdc5620273d3cf1d8b9c583ce2d3695a9e13641146433fbcc939dce249b3ef97d2fe363630c75d8f681b202aec4617ad3df1ed5d5fd65612433f51f5f066ed0856365553ded1af3b557135e7f57c935984f0c70e0e68b77e2a689daf3efe8721df158a136ade73530acca4f483a797abc0ab182b324fb61d108a94bb2c8e3fbb96adab760d7f4681d4f42a3de394df4ae56ede76372bb190b07a7c8ee0a6d709e02fce1cdf7e2ecc03404cd28342f619172fe9ce98583ff8e4f1232eef28183c3fe3b1b4c6fad733bb5fcbc2ec22005c58ef1837d1683b2c6f34a26c1b2effa886b423861285c97ffffffffffffffff
g = 2

# Classic DH key exchange
x = randint(2, p-2)
gx = pow(g, x, p)


if __name__ == "__main__":
    print("p: " + hex(p)[2:])
    print(f"g: {g}")
    
    hex_b = input("Your g^y mod p (in HEX): ")
    print("gx: " + hex(gx)[2:])
    gy = int(hex_b, 16)
    
    shared = pow(gy, x, p)
    sha = sha256(long_to_bytes(shared)).digest()
    key = sha
    iv = os.urandom(16)
    
    aes = AES.new(key, AES.MODE_CBC, iv=iv)
    
    message = b"You've done everything correctly! Good job!! ^-^"
    cipher = aes.encrypt(message)
    
    iv_b64 = base64.b64encode(iv).decode()
    cipher_b64 = base64.b64encode(cipher).decode()
    
    print("IV: " + iv_b64)
    print("Message: " + cipher_b64)
    
    challenge = input("What was my original message? ")
    if challenge == message.decode():
        print("Good job!!")
    else:
        print("Something's wrong! :(")