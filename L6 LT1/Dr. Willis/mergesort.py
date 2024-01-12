def merge(arr, leftArr, rightArr):
    i = j = 0
    k = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1

    while i < len(leftArr):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while j < len(rightArr):
        arr[k] = rightArr[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) >= 2:
        mid = len(arr) // 2
        leftArr = arr[0:mid]
        rightArr = arr[mid:len(arr)]
        mergeSort(leftArr)
        mergeSort(rightArr)
        merge(arr, leftArr, rightArr)


if __name__ == "__main__":
    arr = [5, 8, 1, 5, 9, 43]

    mergeSort(arr)

    print(arr)