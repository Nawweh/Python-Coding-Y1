space=""
count=10
for i in range (0,10):
    print(space, end="")
    space +=" "
    for x in range (0,count):
        print(x, end=" ")
    count-=1
    print()