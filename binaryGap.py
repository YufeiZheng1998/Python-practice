def binaryGap(N):
    binary = []
    while N!=0:
        binary.insert(0, N%2)
        N = N // 2
    if binary.count('1') == 1:
        return 0
    latest = binary.index(1)
    i = latest + 1
    max_len = 0
    while i < len(binary):
        if binary[i] == 1:
            max_len = max(max_len, i - latest)
            latest = i
        i += 1
    return max_len
def binaryGap_simplified(N):
    A = [i for i in range(32) if(N >> i) & 1]
    if len(A) <2 : return 0
    return max(A[i+1]-A[i] for i in range(len(A)-1))
print(binaryGap(5))