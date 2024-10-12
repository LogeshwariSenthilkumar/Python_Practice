def productsmallestpair(sum,arr,n):
    if(n<=2):
        return -1
    else:
        sortarr=sorted(arr)
        n1=sortarr[0]
        n2=sortarr[1]
        sums=n1+n2
        if(sums<=sum):
            product=n1*n2
            return product
        else:
            return 0
sum=int(input())
n=int(input())
arr=[]
for i in range(n):
    arritem=int(input())
    arr.append(arritem)
print(productsmallestpair(sum,arr,n))
    
        
        
