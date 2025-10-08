def fileT2():
    valid="False"

    f=open("f:\\test2.txt","r")

    username=input("give a username: ")
    password=input("give a password: ")
    user_pass=(username,password)
    print(user_pass)
    user_pass_check=[]
    for line in f:
        user_pass_check.append(line)
    for item in user_pass_check:
            if user_pass_check[line]==user_pass:
            valid="True"
            
    if valid=="True":
        print("woohoo access!")
    else:
        print("no access!")
    f.close()


fileT2()

