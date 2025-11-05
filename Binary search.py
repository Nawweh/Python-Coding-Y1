list=[7,10,13,17,23,40,53,71,100,201]
num=100
found=False
while found==False:
    len_list=(len(list))
    if list[int(len_list//2)]>num:
          list2=[] 
          print("hi")      
          for i in range (int(len_list//2)):
              list2.append(list[i])
              print(list2)
              
          break
        