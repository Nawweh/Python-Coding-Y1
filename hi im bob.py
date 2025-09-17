import datetime
def main():
    num_1=int(input("give the first number: "))
    num_2=int(input("give the second number: "))
    num_3=int(input("give the third number: "))
    sum=num_1+num_2+num_3
    average=sum/3
    print("the sum of the two numbers is", str(sum) , "and the average of the two numbers is" , str(average))


def birth():
    current_date = datetime.datetime.now() 
    birth_year= int(input("what is your year of birth: "))
    birth_month= int(input("what is your month of birth: "))
    birth_day= int(input("what is your day of birth: "))

    b_day=datetime.datetime((birth_year), (birth_month), (birth_day))
    age=current_date-b_day
    print(age)
birth()
