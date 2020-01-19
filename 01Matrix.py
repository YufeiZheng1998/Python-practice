def updateMatrix(matrix):
    from collections import deque
    queue = deque()
    dist = [[0 for i  in range(matrix[0])]for _ in range(matrix)]
    for i in range(matrix):
        for j in range(matrix[i]):
            if matrix[i][j] == 0:
                dist[i][j] = 0
                queue.appendleft((i, j))
            else:
                dist[i][j] = 9000
    dir[4][2] = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while not queue:
        x, y = queue[-1]
        queue.pop()
        for i in range(4):
            new_x, new_y = x+dir[i][0], x + dir[i][1]
            if new_x >=0 and new_x<4 and new_y>=0 and new_y<4:
                if dist[new_x][new_y] > dist[x][y] +1:
                    dist[new_x][new_y] = dist[x][y]+1
                    queue.appendleft((new_x,new_y))
    return dist

