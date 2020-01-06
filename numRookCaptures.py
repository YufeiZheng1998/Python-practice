def numRookCaptures(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    x, y = 0 ,0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                x, y = i, j
                break
    num = 0
    pos = y-1
    while pos>=0 and board[x][pos]!='B':
        if board[x][pos] == 'p':
            num+=1
            break
        pos=pos-1
    pos = y+1
    while pos<=7 and board[x][pos]!='B':
        if board[x][pos] == 'p':
            num+=1
            break
        pos = pos+1
    pos = x - 1
    while pos>=0 and board[pos][y]!='B':
        if board[pos][y] == 'p':
            num+=1
            break
        pos = pos-1
    pos = x + 1
    while pos<=7 and board[pos][y]!='B':
        if board[pos][y] == 'p':
            num+=1
            break
        pos = pos + 1
    return num
print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))

