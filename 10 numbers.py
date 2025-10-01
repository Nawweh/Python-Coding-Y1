
list_num=[]
for i in range (0,10):
    num=int(input(f"give number {i+1} "))
    list_num.append(num)

option=input("do you want \n A: count \n B: sum \n C: Average \n D: Min number \n E: Max number")

def get_count(list_num):
    count=0
    for num in list_num:
        count+=1
    print(count)

def get_sum(list_num):
    count=0
    for num in list_num:
        print(num)

get_sum(list_num)