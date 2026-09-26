from collections import deque

class Solution:
    def minCost(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (0, 1),   # 1 → right
            (0, -1),  # 2 → left
            (1, 0),   # 3 → down
            (-1, 0)   # 4 → up
        ]

        distance = [[float('inf')] * cols for _ in range(rows)]

        distance[0][0] = 0

        queue = deque()
        queue.append((0, 0))

        while queue:
            r, c = queue.popleft()

            for direction in range(4):
                dr, dc = directions[direction]

                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Arrow value is 1,2,3,4
                # direction index is 0,1,2,3
                if grid[r][c] == direction + 1:
                    cost = 0
                else:
                    cost = 1

                new_cost = distance[r][c] + cost

                if new_cost < distance[nr][nc]:
                    distance[nr][nc] = new_cost

                    if cost == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))

        return distance[rows - 1][cols - 1]