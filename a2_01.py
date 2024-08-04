a = int(input("Enter first number:  "))
b = int(input("Enter second number:  "))
c = int(input("Enter third number:  "))

if a>b and a>c:
    if b>c:
        print("The ascending order is: ",c,b,a)
        
    else:
        print("The ascending order is: ",b,c,a)
        
elif b>a and b>c:
    if a>c:
        print("The ascending order is: ",c,a,b)
        
    else:
        print("The ascending order is: ",a,c,b)

        
else:
    if a>b:
        print("The ascending order is: ",b,a,c)
        
        
