from collections import deque
from sys import stdin

m, n = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(m)]
R = int(stdin.readline().strip())

visited = [[False] * n for _ in range(m)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start_x, start_y):
    queue = deque([[R, start_x, start_y]])
    visited[start_x][start_y] = True
    total = 1  

    while queue:
        strength, x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != -1:
                if strength > 0:
                    if grid[nx][ny] == 0:  
                        visited[nx][ny] = True
                        total += 1
                        queue.append([strength - 1, nx, ny])
                    elif grid[nx][ny] > 0:  
                        visited[nx][ny] = True
                        total += 1
                        queue.append([grid[nx][ny] - 1, nx, ny])
    return total


start_x, start_y = -1, -1
for i in range(m):
    for j in range(n):
        if grid[i][j] == -2:
            start_x, start_y = i, j
            break
    if start_x != -1:
        break


print(bfs(start_x, start_y))
