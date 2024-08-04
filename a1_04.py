

x = int(input("Enter a number:  "))
y = int(input("Enter another number:  "))
print("Value of x:", x)
print("Value of y:", y)
x = x ^ y
y = x ^ y
x = x ^ y

print("\nValue of x:", x)
print("Value of y:", y)
