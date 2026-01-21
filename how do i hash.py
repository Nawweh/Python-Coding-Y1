import bcrypt

password=input("password: ")
password=password.encode("utf-8")
salt=bcrypt.gensalt()
hash=bcrypt.hashpw(password, salt)
print(hash)

password2=input("password: ")
password2=password2.encode("utf-8")
hash2=bcrypt.checkpw(password2, hash)
print(hash2)
