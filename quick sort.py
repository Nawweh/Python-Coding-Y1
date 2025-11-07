import random

list=[]

for i in range (0,1000):
    list.append(random.randint(0,10000))


def sort(list):
    list_larger=[]
    list_smaller=[]
    list_equal=[]

    if len(list)>1:     
        pivot=list[len(list)-1]

        for item in list:
            if item>pivot:
                list_larger.append(item)
            elif item==pivot:
                list_equal.append(item)
            elif item<pivot:
                list_smaller.append(item)
        
        return sort(list_smaller)+list_equal+sort(list_larger)
        
    else:
        return list

print(sort(list))
