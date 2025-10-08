def fileT2():
    valid=False

    f=open("f:\\test2.txt","r")

    username=input("give a username: ")
    password=input("give a password: ")
    user_pass=(username,password)
    print(user_pass)

    for line in f:
        print(line)
    
    for line in f:
        if line==user_pass:
            valid=True
            
    if valid==True:
        print("woohoo access!")
    else:
        print("no access!")
    f.close()


fileT2()

