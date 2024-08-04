p = int(input("Enter the principle amount:  "))

if p<200000:
    si = p*0.1
    print("The simple interest is: ",si)
elif p>=200000 and p<1000000:
    si = p*0.12
    print("The simple interest is: ",si)
else:
    si = p*0.15
    print("The simple interest is: ",si)
