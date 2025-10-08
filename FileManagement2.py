
def admin_prompt():
    f=open("f:\\test2.txt","a")
    append="true"
    user_add=input("add a new username: ")
    pass_add=input("add a new password: ")
    user_pass_add=(user_add+pass_add)
    print(f"'{user_pass_add}' has been added")
    f.write("\n")
    f.write(user_pass_add)

    f.close()

def encrypt(userpass):
    to_encrypt=(userpass)
    encrypt_userpass=[]
    for letter in to_encrypt:
        letter_ascii=ord(letter)
        letter_ascii*=17
        encrypt_userpass.append(letter_ascii)
    return encrypt_userpass

# def decrypt(encrypt_userpass):
#     decrypt_userpass=[]
#     for letter in encrypt_userpass:
#         decrypt_userpass.append(int(letter/17))
#     print(decrypt_userpass)

def fileT2():
    valid="False"

    f=open("f:\\test2.txt","r")

    username=input("give a username: ")
    password=input("give a password: ")
    user_pass=(username+password)
    user_pass=encrypt(user_pass)

 
    for line in f:
        line=line.strip()
        print(line)
        
        if user_pass=="[1785, 1853, 1649, 1649, 1700, 1853, 1785, 1870]":
            valid="admin"
            break
        elif line==user_pass:
            valid="True"
            print("test")
    f.close()

            
    if valid=="admin":
        print("you an admin")
        admin_prompt()
    elif valid=="True":
        print("woohoo access")
    
    else:
        print("no access!")


fileT2()





