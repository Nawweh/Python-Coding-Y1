def dictT1():
    dict= {0:10,1:20}
    dict.update({2:30})
    print(dict)
    test=int(input("check if something is in this dictionary idk "))
    for i in dict:
        if test == i:
            print("yaya")

def dictT2():
    dict1={1:10,2:20} 
    dict2={3:30,4:40} 
    dict3={5:50,6:60}
    dict={}
   

    for i in (dict1,dict2,dict3):
        print(i)
        dict.update(i)
    print(dict)




def dictT3():
    dict={}
    n=int(input("idk put a number "))
    for i in range (1,n+1):
        dict.update({i:i*i})
    print(dict)



def dictT4():
    dict1 = {'a': 100, 'b': 200, 'c':300, 'e':700, 'r':600} 
    dict2 = {'a': 300, 'b': 200, 'd':400, 'x':560} 
    dict={}
    temp=['a','b','c']

    for x in dict1:
        for i in dict2:
            if i==x:
                dict.update({i: dict1[x]+dict2[i]})
                break
            else:
                if i in dict:
                    dict.update({x:dict1[x]})
                else:
                    dict.update({i:dict2[i]})
            

 
   



    print(dict)



dictT4()