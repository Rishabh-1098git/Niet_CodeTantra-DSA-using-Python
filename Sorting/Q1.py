a = list(map(int, input("Enter the list of numbers: ").split(" ")))
for i in range(len(a)):
    swapped = False
    for j in range(1,len(a)-i):
        if(a[j]<a[j-1]):
            temp = a[j]
            a[j] = a[j-1]
            a[j-1] = temp
            swapped = True
    if(swapped==False):
        break
    
print("Sorted list:",a)
