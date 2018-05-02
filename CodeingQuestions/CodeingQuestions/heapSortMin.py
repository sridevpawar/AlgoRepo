from random import *
def heapSort(arr):
    for i in range(len(arr), -1, -1):
        heapify(arr, len(arr), i)
    checkMinHeap(arr, len(arr))
    for i in range(len(arr)-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
        checkMinHeap(arr, i)

def heapify(arr, n, i):
    min = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] > arr[l]:
        min = l

    if r < n and arr[min] > arr[r]:
        min = r

    if min != i:
        arr[min], arr[i] = arr[i], arr[min]

        heapify(arr, n, min)

def checkMinHeap(arr, n):
    for i in range(n):
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] > arr[l]:
            print("Error")

        if r < n and arr[i] > arr[r]:
            print("Error")

    return True

def insertKey(arr, n, x):
    arr.append(x)
    arr[n], arr[0] = arr[0], arr[n]
    for i in range(n+1, -1, -1):
        heapify(arr, n + 1, i)

def deleteKey(arr, n, i):
    if i < n:
        print(arr[i])
        arr[n-1], arr[i] = arr[i], arr[n-1]
        heapify(arr, n - 1, i)


#arr = []
#for i in range(100):
#    arr.append(randint(0,100))
#print(arr)
#heapSort(arr)
#print(arr[::-1])
#if arr[::-1] == sorted(arr):
#    print("Done")
#else:
#    print("Not sorted")

arr = [ 12, 11, 13, 5, 6, 7]
for i in range(len(arr), -1, -1):
    heapify(arr, len(arr), i)
checkMinHeap(arr, len(arr))
insertKey(arr, len(arr), 300)
checkMinHeap(arr, len(arr))
insertKey(arr, len(arr), 3)
checkMinHeap(arr, len(arr))
insertKey(arr, len(arr), 0)
checkMinHeap(arr, len(arr))
insertKey(arr, len(arr), 100)
checkMinHeap(arr, len(arr))
insertKey(arr, len(arr), 1)
checkMinHeap(arr, len(arr))
deleteKey(arr, len(arr), 6)
checkMinHeap(arr, len(arr)-1)
deleteKey(arr, len(arr) - 1, 2)
checkMinHeap(arr, len(arr)-2)
deleteKey(arr, len(arr) - 2, 0)
checkMinHeap(arr, len(arr)-3)
print(arr)