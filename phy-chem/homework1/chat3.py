def large_combinations(n, r):
    if r > n - r:
        r = n - r  # 由于 C(n, r) == C(n, n - r)
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:  # 这将确保更改为1之后再次不进行相同的操作
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] = 1

    result = 1
    for k in range(r):
        if numerator[k] > 1:  # 确保没有剩余的项可以被简化
            result *= numerator[k]

    return result
n=114
r=1
print(large_combinations(n, r))