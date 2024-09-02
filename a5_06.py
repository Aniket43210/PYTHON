a = int(input("Enter the number of elements in list1:  "))

s = []
d = []

print("\nEnter elements for list:  ")
for i in range(a):
    j = int(input("Enter a number:  "))
    s.append(j)

print("\nList 1:  ")
print(s)

for i in range(a):

    for j in range(a):
        p = s[i]*s[j]
        if p%2 != 0:
            l = [s[i],s[j]]

            d.append(l)

print("\nThe pairs are:  ")
for rows in d:
    print(rows)