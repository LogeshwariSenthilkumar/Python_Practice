r=int(input())
unit=int(input())
n=int(input())
total_units=r*unit
arr=[]
sum=0
count=0
for i in range(n):
    arr_item=int(input())
    arr.append(arr_item)
for i in range(len(arr)):
    sum+=arr[i]
    count+=1
    if(sum>=total_units):
       print(count)
       break
