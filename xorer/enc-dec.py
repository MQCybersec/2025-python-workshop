from xor import xor

message = input("Message (in HEX): ")
key = input("Key (in HEX): ")

# Take the two inputs as HEX and convert them both to bytes! Then, find the XOR of the bytes.
# Change these two lines
# vvvvvvvvvvvvvvvvvvvvvv
message_bytes = None
key_bytes = None

cipher = xor(message_bytes, key_bytes)

# Print the ciphertext in HEX (or whatever encoding you want, really)