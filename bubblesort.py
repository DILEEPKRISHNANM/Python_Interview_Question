arr = [5,3,2,6,4,1]
n=len(arr)
for i in range(0,n):
    for j in range(0,n-i-1):
        if arr[j] <arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]


print(arr)