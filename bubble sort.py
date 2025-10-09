import random
unsorted=[]
for i in range (random.randint(0,50)):
    unsorted.append(random.randint(0,100))

sorted=[]
count=0
hold=0
string_length=len(unsorted)
count2=5
for i in unsorted:
    count=0
    for x in range (string_length-1):
        if unsorted[x+1]>unsorted[x]: #checks if the number adjacent to the right in the list is larger
            hold=unsorted[count+1]
            unsorted[count+1]=unsorted[count] #if it is larger the 2 numbers are swapped around (bubble sort)
            unsorted[count]=hold
        count+=1

for i in range (1,string_length+1):
    sorted.append(unsorted[-i])


print (unsorted)
print(sorted)