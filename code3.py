count_odd=0
count_even=0
for i in range(1,11):
    if(i%2!=0):
        count_odd+=1
    else:
        count_even+=1
print("Odd count:",count_odd)
print("Even count:",count_even)
