def leftrotate(arr, k, n ):
    for x in range(k):
        rotateone(arr, n)

def rotateone(arr, n):
    temp = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]
    arr[n-1] = temp

arr = list(map(int,input().split()))
k = int(input())
leftrotate(arr, k, len(arr))
print(arr)          

