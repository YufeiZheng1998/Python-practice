def addStr(num1,num2):
    i, j = len(num1)-1, len(num2)-1
    result, extra = '', 0
    while i >=0 or j >=0:
        if i>=0:
            extra += ord(num1[i]) - ord('0')
        if j>=0:
            extra+= ord(num2[j]) - ord('0')
        result += str(extra % 10)
        extra = extra // 10
        i-=1
        j-=1
    if extra!=0:
        result += str(extra)
    return result[::-1]