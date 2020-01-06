# ab#c
# ad#c
def backspaceCompare(S,T):
    S_final = []
    T_final = []
    for i in range(len(S)):
        if S[i]!='#':
            S_final.append(S[i])
        if S[i] =='#':
            if S_final:
                S_final.pop()
    for i in range(len(T)):
        if T[i]!='#':
            T_final.append(T[i])
        if T[i] =='#':
            if T_final:
                T_final.pop()
    return S_final==T_final
print(backspaceCompare("#bc","#bc"))


