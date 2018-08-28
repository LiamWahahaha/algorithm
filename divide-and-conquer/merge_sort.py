def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    i, j, k = 0, 0, 0
    res = [None] * (len(left) + len(right))

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        for idx in range(i, len(left)):
            res[k] = left[idx]
            k += 1

    if j < len(right):
        for idx in range(j, len(right)):
            res[k] = right[idx]
            k += 1

    return res
