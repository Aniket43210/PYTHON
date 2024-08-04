p = int(input("Enter a number:  "))
i = int(input("Enter another number:  "))
gcd = 0
if p>i:
    gcd = p%i 
    while gcd!=0:
        gcd  = p%i
        p = i
        i = gcd
elif p<i:
    gcd = i%p
    while gcd!=0:
        gcd  = i%p
        i = p
        p = gcd

else:
    print("The GCD: 1")

print("The GCD is :  ",gcd)
