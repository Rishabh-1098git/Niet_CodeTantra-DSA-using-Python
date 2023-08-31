
print("Enter values for matrix - A")
r1 = int(input("Number of rows, m = "))
c1 = int(input("Number of columns, n = "))
lst = [] 
for i in range(r1):
    lst.append([0 for i in range(c1)])

for i in range(r1):
    for j in range(c1):
        print(f"Entry in row: {i+1} column: {j+1}")
        lst[i][j] = int(input())
        
print("Enter values for matrix - B")
r2 = int(input("Number of rows, m = "))
c2 = int(input("Number of columns, n = "))
lst2 = []

for i in range(r2):
    for j in range(c2):
        print(f"Entry in row: {i+1} column: {j+1}")
        lst2[i][j] = int(input())
print("Matrix - A =",lst)
print("Matrix - B =",lst2)

lst3 = []
for i in range(r1):
    lst3 .append([0 for i in range(c2)])

x1=0
y1=0
for i in range(r1):
    for j in range(c2):
        for k in range(r1):
            lst3[i][j]+= lst[i][k]*lst2[k][j]

print("Matrix - A * Matrix - B =",lst3)












            
            lst3[i][j] += lst[i][k]*lst2[k][j]
