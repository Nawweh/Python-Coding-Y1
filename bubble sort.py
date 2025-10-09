unsorted=[7,4,1,98,5,12,65,68,13,90,2,123,65,234]
sorted=[]
hold=0
for i in unsorted:
    for x in unsorted:
        if i<x:
            hold=i
    sorted.append(hold)
print(sorted)