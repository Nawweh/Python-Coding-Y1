space="                      "
for i in range (1,11): 
    print(space,end=" ")
    space=space[:-2]

    for x in range (1,i):
        print(x, end=" ")  

        if x+1==i:

            while x>0:
                 x-=1
                 
                 if x==0:
                     break
                 else:
                    print(x, end=" ")                 
    print()


