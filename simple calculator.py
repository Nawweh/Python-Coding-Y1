def calculator():
    num1=int(input("give me num1: "))
    num2=int(input("give me num2: "))
    operator=input("give me an operator: ")
    if operator=="+":
        calculation=num1+num2
    elif operator=="-":
        calculation=num1-num2
    elif operator=="*":
        calculation=num1*num2
    elif operator=="/":
        calculation=num1/num2
    else:
        print("you did it wrong :(")

    print(calculation)
calculator()

