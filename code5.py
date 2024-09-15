a=[]
n=int(input())
for i in range(1,n+1):
    num=int(input("Enter num"+str(i)+":"))
    a.append(num)
print(a)
sum=0
for i in a:
    sum=sum+i
print(sum)
