def arangeCoin(n):
    k = 1
    while k*(k+1)/2 < n:
        k += 1
    if k*(k+1)/2 == n:
        return k
    else:
        return k-1
print(arangeCoin(5))