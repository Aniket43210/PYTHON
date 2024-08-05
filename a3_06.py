i  = int(input("Enter the range:  "))
p = 0
a = 0
b = 1
c= 0
while c<=i:
    c = a+b
    if c%2 == 0 and c<=i:
        p = p+c
        
    a = b
    b = c

print("The sum is: ",p)