n=input()
a=int(n[0])
for i in range(1,len(n),2):
    if(n[i]=='A'):
        p=a & int(n[i+1])
    elif(n[i]=='B'):
        p=a|int(n[i+1])
    elif(n[i]=='C'):
        p=a^int(n[i+1])
print(p)
    
