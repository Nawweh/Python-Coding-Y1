def admin_prompt():
    f=open("f:\\test2.txt","a")
def fileT2():
    valid="False"

    f=open("f:\\test2.txt","r")

    username=input("give a username: ")
    password=input("give a password: ")
    user_pass=(username+password)
    user_pass_check=[]
    for line in f:
        
        if user_pass=="imaadmin":
            valid="admin"
            break
        elif line==user_pass:
            valid="True"
    f.close()

            
    if valid=="admin":
        print("you an admin")
        admin_prompt()
    elif valid=="True":
        print("woohoo access!")
    
    else:
        print("no access!")


admin_prompt()

def admin_prompt():
    f=open("f:\\test2.txt","a")
    append="true"
    while append=="true":
        user_add=input("add a new username: ")
        pass_add=input("add a new password: ")
        user_pass_add=(user_add+pass_add)
        print("user_pass_add")
    f.close()



