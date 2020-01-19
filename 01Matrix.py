def updateMatrix(matrix):
    from collections import deque
    queue = deque()
    dist = [[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                dist[i][j] = 0
                queue.appendleft((i, j))
            else:
                dist[i][j] = 9000
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        x, y = queue[-1]
        queue.pop()
        for i in range(4):
            new_x, new_y = x+dir[i][0], y + dir[i][1]
            if new_x >=0 and new_x<len(matrix) and new_y>=0 and new_y<len(matrix[0]):
                if dist[new_x][new_y] > dist[x][y] +1:
                    dist[new_x][new_y] = dist[x][y]+1
                    queue.appendleft((new_x,new_y))
    return dist
print(updateMatrix([[0,0,0], [0,0,0], [0,0,0]]))
