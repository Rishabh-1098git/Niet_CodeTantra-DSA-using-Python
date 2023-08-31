print("Enter values for Matrix ")
m = int(input("Number of rows, m = "))
n = int(input("Number of columns, n = "))
lst = []
for i in range(m):
    lst.append([0 for i in range(n)])
# print(lst)
for i in range(m):
    for j in range(n):
        print(f"Entry in row: {i+1} column: {j+1}")
        lst[i][j] = int(input())
        
print("Matrix  =",lst)
print("Sparse Matrix: ")
for i in range(m):
    for j in range(n):
        if lst[i][j] != 0:
            print(f"{i} {j} {lst[i][j]} ")
