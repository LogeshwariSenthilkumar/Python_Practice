def findcount(arr,n,num,diff):
    count=0
    for i in range(n):
        if(abs(arr[i]-num)<=diff):
            count+=1
    if count:
        return count
    return -1

arr=[]
n=int(input())
for i in range(n):
    arr_item=int(input())
    arr.append(arr_item)
num=int(input())
diff=int(input())
print(findcount(arr,n,num,diff))
