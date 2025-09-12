import math
def moneyulator():
    option=input("do you want to: \n A: convert from pounds to euros \n B: convert pounds to yen \n (type your answer as A or B): ")
    NumPounds=float(input("how many pounds do you have?: "))
    if option=="A":
        NumEuros=NumPounds*1.26
        NumEuros=round(NumEuros, 2)
        print(NumEuros)
    elif option=="B": 
        NumYen=NumPounds*124.6
        NumYen=round(NumYen, 2)
        print(NumYen)
    else:
        print("there hasuth been error bro rip in peace!")
    
moneyulator()


