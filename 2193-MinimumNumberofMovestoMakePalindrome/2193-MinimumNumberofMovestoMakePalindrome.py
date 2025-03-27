# Last updated: 3/26/2025, 10:53:52 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, i, j ):
            if i >= m or j >= n or i < 0 or j < 0 or grid[i][j] != "1":
                return

            grid[i][j] = "0"

            dfs(grid, i+1,j)
            dfs(grid,i,j+1)
            dfs(grid,i-1,j)
            dfs(grid,i,j-1)           


        islands = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    islands += 1

        return islands


        