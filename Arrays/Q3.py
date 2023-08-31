n = int(input("Enter how many elements you want:"))
print("Enter numbers in array:")
lst = []
for i in range(n):
    lst.append(int(input("num:")))
    
print("ARRAY:",lst)
t = int(input("Enter position you want to delete element:"))
lst.pop(t)
print(lst)
    
