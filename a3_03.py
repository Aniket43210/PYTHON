a = int(input("Enter a number:  "))
b = int(input("Enter another number:  "))
p = 0
if a>b:
    p=a
    while p>=a:
        if p%a == 0 and p%b == 0:
            break
        p = p+1    

else:
    p=b
    while p>=b:
        if p%a == 0 and p%b == 0:
            break
        p = p+1
        

print("The LCM is: ",p)