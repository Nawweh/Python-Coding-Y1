list=[7,10,13,17,23,40,53,71,100,201]
num=100
found=False
while found==False:
    len_list=(len(list))
    if list[int(len_list//2)]>num:
        list= list[0:len_list//2]
    elif list[int(len_list//2)]<num:
        list= list[len_list//2:]
    else:
        found=True
print("the number has been found")