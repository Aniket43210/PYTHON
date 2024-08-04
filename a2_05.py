p = int(input("Enter a number:  "))
i = int(input("Enter another number:  "))
gcd = 0

if p>i:
    for k in range(1,p):
        if p%k == 0 and i%k == 0:
            gcd = k

elif i>p:
    for k in range(1,i):
        if p%k == 0 and i%k == 0:
            gcd = k

else:
    print("No GCD")

print("The GCD is :  ",gcd)