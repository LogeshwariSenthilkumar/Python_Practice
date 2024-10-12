def largesmall(arr,n):
    evenlist=[]
    oddlist=[]
    if(n==0):
        return 0
    else:
        for i in range(0,n,2):
            evenlist.append(arr[i])
        sortevenlist=sorted(evenlist)
        for i in range(1,n,2):
            oddlist.append(arr[i])
        sortoddlist=sorted(oddlist)
        sum=sortevenlist[len(evenlist)-2]+sortoddlist[len(oddlist)-2]
        return sum
        


arr=[]
n=int(input())
for i in range(n):
    arritem=int(input())
    arr.append(arritem)
print(largesmall(arr,n))
