def addToArrayForm(A, K):
        i = len(A)-1
        while i>=0:
                K = K + A[i]
                A[i] = K % 10
                K = K // 10
                i = i - 1

        while K != 0:
                A.insert(0,K % 10)
                K  = K // 10
        return A
print(addToArrayForm([1,2,3,0], 999))