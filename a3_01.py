i = int(input("Enter a number:  "))

for j in range(2,i):
    if i%j  == 0:
        print("The number is not prime")
        break
    
else:
    print("The number is prime")