class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rowLen, colLen = len(grid), len(grid[0])
        # visited = set()
        def dfs(r, c):
            if r<0 or r>=rowLen:
                return 
            if c<0 or c>=colLen:
                return                
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rowLen):
            for c in range(colLen):
                # if grid[r][c] == "1" and (r, c) not in visited:
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)

        return count
