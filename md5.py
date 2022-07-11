# hashing library
import hashlib

value = input("input your data : ")
# the functiion expects a encoded byte value,
# so i am using the `.encode()` function on 
# inout value
hashed_bytes = hashlib.md5(value.encode())

# the result would be in bytes so to convert
# it back to readable format we can use `hex`
# method
hash_data = hashed_bytes.hexdigest()
print("Hashed value is", hash_data)