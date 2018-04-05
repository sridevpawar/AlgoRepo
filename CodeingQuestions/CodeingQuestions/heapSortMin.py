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



arr = []
for i in range(100):
    arr.append(randint(0,100))
print(arr)
heapSort(arr)
print(arr[::-1])
if arr[::-1] == sorted(arr):
    print("Done")
else:
    print("Not sorted")