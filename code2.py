number1=int(input("Enter Number1:"))
number2=int(input("Enter Number2:"))
choice=input("Enter Choice add/sub/mul/div:")
if(choice=="add"):
    result=number1+number2
    print("Addition of two numbers:",result)
elif(choice=="sub"):
    result=number1-number2
    print("Subraction of two numbers:",result)
elif(choice=="mul"):
    result=number1*number2
    print("Multiplication of two numbers:",result)
elif(choice=="div"):
    result=number1/number2
    print("Division of two numbers:",result)
