def nth_fibonacci(n):
    f_pre = 0
    f_cur = 1

    if n == 1:
        return f_cur
    else:
        count = 1
        while count < n:
            count += 1
            f_tmp = f_cur
            f_cur = f_pre + f_cur
            f_pre = f_tmp

    return f_cur

print(nth_fibonacci(9) == 34)
print(nth_fibonacci(2) == 1)
