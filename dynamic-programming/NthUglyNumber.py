def nth_ugly_number(n):
    ugly = [None] * n
    ugly[0] = 1
    idx_2 = 0
    idx_3 = 0
    idx_5 = 0

    next_multiple_of_2 = ugly[idx_2] * 2
    next_multiple_of_3 = ugly[idx_3] * 3
    next_multiple_of_5 = ugly[idx_5] * 5

    for idx in range(1, n):
        next_ugly_no = min(next_multiple_of_2,\
                           next_multiple_of_3,\
                           next_multiple_of_5)
        ugly[idx] = next_ugly_no

        if next_ugly_no == next_multiple_of_2:
            idx_2 += 1
            next_multiple_of_2 = ugly[idx_2] * 2

        if next_ugly_no == next_multiple_of_3:
            idx_3 += 1
            next_multiple_of_3 = ugly[idx_3] * 3

        if next_ugly_no == next_multiple_of_5:
            idx_5 += 1
            next_multiple_of_5 = ugly[idx_5] * 5

    return ugly[-1]

print(nth_ugly_number(150))
