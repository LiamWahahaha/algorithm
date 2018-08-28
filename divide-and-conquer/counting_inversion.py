def sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, count_l = sort_and_count(arr[:mid])
    right, count_r = sort_and_count(arr[mid:])
    res, count_lr = count_and_sort(left, right)

    return res, count_l + count_r + count_lr

def count_and_sort(left, right):
    i = 0
    j = 0
    count = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            count += len(left) - i
            j += 1

    if i != len(left):
        res += left[i:]
    if j != len(right):
        res += right[j:]

    return res, count
