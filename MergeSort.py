def MergeSort(array, left, right):
    mid = (left + right) // 2

    MergeSort(array, left, mid)
    MergeSort(array, mid+1, right)

    merge(array, left, right, mid)

def Merge(array, left, rigth, mid):
    leftArray = array[left:mid+1]
    rigthArray = array[mid+1 : right+1]

    leftIndex = 0
    rightIndex = 0
    ArrayIndex = 0

    while
a = [5, 4, 3, 2, 1]
print(a)
MergeSort(a, 0, len(a))