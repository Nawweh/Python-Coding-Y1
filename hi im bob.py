import datetime
def main():
    num1=int(input("give the first number: "))
    num2=int(input("give the second number: "))
    num3=int(input("give the third number: "))
    sum=num1+num2+num3
    average=sum/3
    print("the sum of the two numbers is", str(sum) , "and the average of the two numbers is" , str(average))


def birth():
    currentdate = datetime.datetime.now() 
    birthyear= int(input("what is your year of birth: "))
    birthmonth= int(input("what is your month of birth: "))
    birthday= int(input("what is your day of birth: "))

    bday=datetime.datetime((birthyear), (birthmonth), (birthday))
    age=currentdate-bday
    print(age)
birth()
