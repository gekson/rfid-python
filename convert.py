hex_string = "34413834304a343943000000"

bytes_object = bytes.fromhex(hex_string)

ascii_string = bytes_object.decode("ASCII")

print(ascii_string)