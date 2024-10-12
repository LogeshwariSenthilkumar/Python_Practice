def operation(c,a,b):
    if(c==1):
        return(a+b)
    elif(c==2):
        return(a-b)
    elif(c==3):
        return(a*b)
    elif(c==4):
        return(a/b)

c=int(input())
a=int(input())
b=int(input())
print(operation(c,a,b))
