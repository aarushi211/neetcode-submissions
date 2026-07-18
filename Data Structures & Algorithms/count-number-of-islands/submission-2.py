class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowLen, colLen = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (0<=nr<rowLen) and (0<=nc<colLen) and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
        
        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count


