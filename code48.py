str=input()
listh=''
listnh=''
for i in str:
    if(i=="-"):
        listh+=i
    else:
        listnh+=i
        
print(listh+listnh)

