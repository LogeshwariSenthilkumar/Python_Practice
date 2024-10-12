n=int(input())
num=int(input())
remlist=[]
q=num//n
r=num%n
remlist.append(r)
while(q!=0):
    r=q%n
    q=q//n
    remlist.append(r)
remlist=remlist[::-1]
res=''
for i in remlist:
    if i>9:
        a=i-9
        a=64+a
        res+=chr(a)
    else:
        res+=str(i)
print(res)
        
    
