def swap(lst, A, n):
    lst[A], lst[n] = lst[n], lst[A]

def insertionSort(A, n):
    for pos in range(1, n):
        nextpos = pos
        while nextpos > 0 and A[nextpos] < A[nextpos - 1]:
            swap(A, nextpos, nextpos - 1)
            nextpos = nextpos - 1
    return A

lst = [12, 40, 33, 5, 6, 10, 25, 32, 50, 20]
sortedLst = insertionSort(lst, len(lst))
print(f"Original Array:{lst}", )
print(f"Sorted Array:{sortedLst}", )
