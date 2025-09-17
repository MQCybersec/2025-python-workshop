# Binary is base 2. We only have 2 possible values, 0 or 1, and numbers are expressed as a sum of powers of 2, with the character set [01]
# Octal is base 8. Numbers are expressed as a sum of powers of 8, with the character set [0-7]
# Hexadecimal is base 16. Numbers are expressed as a sum of powers of 16, with the character set [0-9a-f]
# In base 32, numbers are expressed as a sum of powers of 32, with the character set [A-Z2-7=]
# In base 64 then, numbers are expressed as a sum of powers of 64, with the character set [A-Za-z0-9+/=]

# e.g. the number 0 in decimal corresponds to A in base 64, and the number 26 in decimal corresponds to a in base64.

# Here is an integer to hexadecimal conversion function. An integer to base64 conversion function will look
# VERY similar to this.
def int2hex(n: int) -> str:
    if n == 0:
        return "0"
    
    CHARSET = "0123456789abcdef"
    res = ""
    
    while n != 0:
        r = n % 16
        res = CHARSET[r] + res
        n >>= 4

# This is the true meaning of base 64: just another number base. 
# Implement the base64 encoding function for a number and a string
def base64encode_int(input: int) -> str:
    pass


def base64encode_str(input: str) -> str:
    pass