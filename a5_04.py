a = []
b = []

s = int(input("Enter the number of elements in list 1:  "))
j = int(input("Enter the number of elements in list 2:  "))

print("\nEnter the elements for list 1:  ")
for i in range(s):
    m = eval(input("Enter a number:  "))
    a.append(m)

print("\nList 1:")
print(a)

print("\nEnter elements for list 2:  ")
for i in range(j):
    m = eval(input("Enter a number:  "))
    b.append(m)

print("\nList 2")
print(b)  

c = []

for i in range(s):
    c.append(a[i])

for i in range(j):
    c.append(b[i])

print("\nThe concatenated list is:  ")
print(c)
