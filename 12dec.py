from collections import deque

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    sx, sy = start
    ex, ey = end

    if grid[sx][sy] == 1 or grid[ex][ey] == 1:
        return -1  # start or end blocked

    visited = [[False]*cols for _ in range(rows)]
    visited[sx][sy] = True

    q = deque()
    q.append((sx, sy, 0))  # (x, y, steps)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right

    while q:
        x, y, steps = q.popleft()
        if (x, y) == (ex, ey):
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<=nx<rows and 0<=ny<cols and not visited[nx][ny] and grid[nx][ny]==0:
                visited[nx][ny] = True
                q.append((nx, ny, steps+1))

    return -1  # unreachable


# ---------------- Demo ----------------
grid = [
    [0,0,0,1],
    [1,0,1,0],
    [0,0,0,0],
    [0,1,1,0]
]
print()

start = (0,0)
end = (3,3)

res = shortest_path(grid, start, end)
print("Minimum steps:", res)
