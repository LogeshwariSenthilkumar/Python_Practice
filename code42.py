def checkpassword(s,n):
    if(n<4):
        return 0
    if(s[0].isdigit()):
        return 0
    cap=0
    nu=0
    for i in range(n):
        if(s[i]==" " or s[i]=="/"):
            return 0
        if(s[i]>="A" and s[i]<="Z"):
            cap+=1
        elif(s[i].isdigit()):
            nu+=1
    if(cap>=1 and nu>=1):
        return 1


str=input()
n=len(str)
print(checkpassword(str,n))
