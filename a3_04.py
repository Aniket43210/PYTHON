i = int(input("Enter the initial number:  "))
p = int(input("Enter the final number:  "))
s = 0
for o in range(i,p):
    for j in range(2,o):
        if o%j  == 0:
            break
    else:
        s = s+o

print("The sum is:",s)