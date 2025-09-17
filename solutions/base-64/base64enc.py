def int2hex(n: int) -> str:
    if n == 0:
        return "0"
    
    CHARSET = "0123456789abcdef"
    res = ""
    
    while n != 0:
        r = n % 16
        res = CHARSET[r] + res
        n >>= 4

import string

def base64encode_int(input: int) -> str:
    if input == 0:
        return "0"
    
    CHARSET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
    res = ""
    
    while input > 0:
        r = input % 64
        res = CHARSET[r] + res
        input >>= 6
        
    return res

# No padding handling. With an input with length not a multiple of 3, encoding will fail
def base64encode_str(input: str) -> str:
    
    i = 0
    res = ""
    
    while i*3 < len(input):
        tmp = input[i*3:i*3+3]
        num = 0
        
        n = len(tmp)
        
        for j in range(n):
           num += ord(tmp[j]) << (n-j-1)*8 
        res += base64encode_int(num)
        i += 1
        
    return res

print(base64encode_str("wordle"))
print(base64encode_str("WORDLE"))