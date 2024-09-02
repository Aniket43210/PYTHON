l1 = []
i = int(input("\nEnter the number of elements :  \n"))

for j in range(i):
    s = eval(input(f"Enter a number for position {j+1}:  "))
    l1.append(s)
max = l1[0]
min = l1[0]

for k in range(i):
    if l1[k]>max:
        max = l1[k]

for k in range(i):
    if l1[k]<min:
        min = l1[k]

print(f"\nThe maximum is: {max}")
print(f"\nThe minimum is: {min}")