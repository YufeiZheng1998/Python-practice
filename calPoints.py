def calPoints(ops):
    score_list = []
    for i in range(len(ops)):
        if ops[i] != 'C' and ops[i]!='D' and ops[i]!='+':
            score_list.append(int(ops[i]))
        if ops[i] == 'C':
            score_list.pop()
        if ops[i] =='D':
            score_list.append(2*score_list[len(score_list)-1])
        if ops[i] =='+':
            score_list.append(score_list[len(score_list)-1]+score_list[len(score_list)-2])
    return sum(score_list)
print(calPoints(["5","2","C","D","+"]))
