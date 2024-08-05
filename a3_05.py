i = int(input("Enter a number:  "))
s = 0
j = 0
z =0 
while i!=-1:
    for j in range(2,i):
        if i%j  == 0:
            z = z+1
            break
    
    else:
        s = s+1
    i = int(input("Enter a number:  "))

print("The number of prime numbers is: ",s)
print("The numbers of composite numbers is: ",z)