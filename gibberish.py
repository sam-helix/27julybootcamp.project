import hashlib
result = hashlib.blake2s(b'shubhamkumar')
print("the byte equivalent is :", end=" ")
print(result.digest())