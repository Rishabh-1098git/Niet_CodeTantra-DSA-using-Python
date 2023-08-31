l = int(input("Enter size of list: "))
lst = [] 
for i in range(l):
    lst.append(int(input("Enter your number: ")))
    
lst.sort()
print("After sorting list is: ",lst )
t = int(input("The number to search for: "))
i=0
j=len(lst)-1
while(i<=j):
    mid = int((i+j)/2)
    if(lst[mid]==t):
        print(f"{t} was found at index {mid}.")
        break
    elif(t>lst[mid]):
        i =mid+1
    else:
        j=mid-1
