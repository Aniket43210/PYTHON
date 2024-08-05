i = int(input("Enter a number:  "))
p = str(i)
l = len(str(i))
s = 0
for j in p:
    s = s+int(j)**l

if s == i:
    print("The number is armstrong")
else:
    print("the number is not armstrong")