count=0
ten_tb=[]

for i in range (1,11):
    for x in range (1,11):
        ten_tb.append(i*x)
        if count==9:
            for z in range(len(ten_tb)):
                print(ten_tb[z], end="\t")
            print()
            ten_tb=[]
            count=0
            continue
        count+=1
        

