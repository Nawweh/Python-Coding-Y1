dictionary={1:20,5:56,2:29,4:"apple",3:"booger"}
dict_key_holder=[]
dict_key=[]
for i in dictionary:
    dict_key_holder.append(i)
for i in dict_key_holder:
    for x in dict_key_holder:
        if dict_key_holder[i-1]>dict_key_holder[x-1]:
            dict_key.append(i)
print(dict_key)