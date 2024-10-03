n=int(input())
fact=1
flag=0
for i in range(1,n+1):
    fact=fact*i
    if(fact==n):
        flag=1
if(flag==1):
    print("Yes")
else:
    print("No")
