def addBinary(a,b):
    result, extra = '', 0
    i, j = len(a)-1, len(b)-1
    while i>=0 or j>=0:
        if i >= 0:
            extra += ord(a[i]) - ord('0')
        if j >= 0:
            extra += ord(b[j]) - ord('0')

        result += str(extra % 2)
        extra = extra // 2
        i-=1
        j-=1
    if extra == 1:
        result += '1'
    return result[::-1]

