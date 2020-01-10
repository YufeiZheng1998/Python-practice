def hasAlternatingBits(n):
    history = -1
    flag = True
    while n!=0:
        if n%2 == history:
            flag = False
            break
        history =n % 2
        n = n // 2
    return flag
print(hasAlternatingBits(11))