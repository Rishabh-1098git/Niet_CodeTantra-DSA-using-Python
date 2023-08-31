# // Insertion sort ==> Rishabh Saini
# taking input string as a list
array = list(map(int, input("Enter the list of numbers: ").split(" ")))
# display array
print(list(map(str,array)))
def swap(arr, a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    
for i in range(len(array)-1):
    j =i+1
    while(j>0):
        if(array[j-1]>array[j]):
            swap(array,j-1,j)
        j-=1
        
print(list(map(str, array)))
