def fileT1():
    f=open("f:\\test.txt","r")
    for line in f:
        print(line)
    f.close()

def fileT2():
    f=open("f:\\U+P.txt","W")
    f.close()

fileT2()