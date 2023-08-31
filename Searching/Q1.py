n = list(map(int,input("Enter the list of numbers: ").split(" ")))
t = int(input("The number to search for: "))
flag = False
for i in range(len(n)):
    if n[i]==t:
        flag = True
        break
if(flag):
    print(f"{t} was found at index {i}.")
else:
    print(f"{t} was not found.")
