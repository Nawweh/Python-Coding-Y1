def log_in():
    user_name=input("give me a username bro please i need this: ")
    pass_word=input("give me a password PLEASE BRO I REALLY NEED A PASSWORD PLEASE HELP ME PLEASE AAAAAAAAAAA: ")
    if user_name=="Admin" and pass_word=="deity" or user_name=="User" and pass_word=="mortal":
        print("Login Successful")
    else:
        print("Incorect username or password :( )")
log_in()