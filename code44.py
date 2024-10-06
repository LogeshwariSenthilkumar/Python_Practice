def differenceofsum(n,m):
    sum_div=0
    sum_notdiv=0
    for i in range(1,m+1):
        if(i%n==0):
            sum_div+=i
        else:
            sum_notdiv+=i
    diff=sum_notdiv-sum_div
    return diff

n=int(input())
m=int(input())
print(differenceofsum(n,m))
