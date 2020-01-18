def count(n):
    count = 0
    while n>0:
        n  = n & (n-1)
        count +=1
    return count
def readBinaryWatch(num):
    result = []
    for i in range(0,12):
        if count(i) == num:
            result.append(str(i)+':'+'00')
            continue
        for j in range(1,60):
            if count(i) + count(j) == num:
                result.append(str(i)+':'+('0'+str(j) if j<10 else str(j)))
    return result
