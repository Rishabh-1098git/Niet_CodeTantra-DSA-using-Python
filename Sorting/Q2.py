arr = list(map(int, input("Enter the list of numbers: ").split(" ")))
def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    
def get_max_index(arr,start,end):
    maxi=0
    for i in range(start,end+1):
        if arr[maxi]<arr[i]:
            maxi = i
    return maxi
    
start = 0
for i in range(len(arr)):
    end = len(arr)-i-1
    swap(arr,end,get_max_index(arr,start,end))
    
ans = list(map(str,arr))
    
print(ans)
