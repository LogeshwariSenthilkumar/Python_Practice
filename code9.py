fact=1
n=int(input("Enter number:"))
print("Factorial of "+str(n)+" is: ",end="")
while(n>0):
    fact=fact*n
    n-=1
print(fact)
