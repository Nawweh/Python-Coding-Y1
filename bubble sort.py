unsorted=[7,4,1,98,5]
sorted=[]
count=0
hold=0
for i in (0,30):
    count=0
    for x in range (0,4):
        if unsorted[x+1]>unsorted[x]:
            hold=unsorted[count+1]
            unsorted[count+1]=unsorted[count]
            unsorted[count]=hold
            print(count)
        count+=1
print(unsorted)