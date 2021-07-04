import hashlib
#program using hashlib's 3 algorithms' to print giberish form of a string data
str_1='shubham'
result = hashlib.md5(str_1.encode())
print("the byte equivalent is :", end=" ")
print(result.hexdigest())
#printing gibberish form of string data using sha3_256() in hexadecimal form

str_2='sam'
result_2=hashlib.sha3_256(str_2.encode())
print("The hexdecimal hash is :", end=" ")
print(result_2.hexdigest())

#printing gibesrish form of string data using blake2b 

str_3='you rocks'
result_3=hashlib.blake2b(str_3.encode())
print("The hexdecimal hash is :", end=" ")
print(result_3.hexdigest())
