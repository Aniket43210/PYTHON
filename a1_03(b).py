a = int(input("Enter a number:  "))
b = int(input("Enter another number:  "))

print("The number before swapping are:",a,b) 
a=a+b
b = a-b
a= a-b
print("The numbers after swapping are: ",a,b)
