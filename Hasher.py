
from hashlib import md5

password = input("Hash: ")
password = password.encode()
password = md5(password)
password = password.hexdigest()
print(password)

input("Press enter to close")