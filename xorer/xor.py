def xor(bytes1: bytes, bytes2: bytes):
    # Implement the XOR function here!  
    # INTENDED BEHAVIOUR: If the bytestreams are not equal length, then "wrap around" the shorter one.
    # For example, given message b"HELLOWORLD" and key b"OAEP", XOR them as such
    
    #               H E L L O W O R L D
    #                       XOR
    #               O A E P O A E P O A
    
    # You may find the bytearray() type useful for this instead: for a bytearray, you can
    # use the .append() method by passing an int directly, and it will automatically turn it
    # to a byte 
    
    pass