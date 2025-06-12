# Last updated: 6/11/2025, 10:34:23 PM
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        maxArea = 0

        def dfs(grid, row, col):
            if row >= m or col >= n or grid[row][col] != 1 or row < 0 or col < 0:
                return 0

            grid[row][col] = 0

            return (1 + dfs(grid,row+1, col) + dfs(grid,row-1, col)+ dfs(grid,row, col+1)+ dfs(grid,row, col-1))

            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(grid, i, j))
        return maxArea


        


        