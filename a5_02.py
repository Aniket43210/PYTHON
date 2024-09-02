l1 = []
l2 = []

i = int(input("Enter the number of rows matrix 1:  "))
j = int(input("Enter the number of columns matrix 1:  "))

a = int(input("\nEnter the number of rows matrix 2:  "))
b = int(input("Enter the number of columns matrix 2:  "))

print("\nEnter the elements for matrix 1:  ")
for r in range(i):
    rows1 = []
    for k in range(j):
        e = int(input(f"Enter the element for position {r+1}X{k+1}:  "))
        rows1.append(e)
    l1.append(rows1)

print("Matrix 1:")
for rows1 in l1:
    print(rows1)

print("\nEnter the elements for matrix 2:  ")
for r in range(a):
    rows1 = []
    for k in range(b):
        e = int(input(f"Enter the element for position {r+1}X{k+1}:  "))
        rows1.append(e)
    l2.append(rows1)

print("\nMatrix 2:")
for rows1 in l2:
    print(rows1)

#multiply

if j!=a:
    print("The matrices cannot be multiplied")
l3 = []
for r in range(i):
    rows2 = []
    for l in range(b):


        s = 0
        for k in range(j):
            s += l1[r][k]*l2[k][l]
            
        rows2.append(s)
    l3.append(rows2)

print("\nThe result of multiplication is:  ")
for rows2 in l3:
    print(rows2)