def prefixDivBy5(A):
    tsum = 0
    for i,num in enumerate(A):
        tsum = (tsum*2+num) % 5
        A[i] = (tsum%5== 0)
    return A
print(prefixDivBy5([0,1,1,1,1,1]))