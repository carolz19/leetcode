class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, coords):
            x,y = coords
            if grid[x][y] == '0': return

            grid[x][y] = '0'

            if x > 0: dfs(grid, (x-1, y))
            if y > 0: dfs(grid, (x, y-1))
            if x < len(grid)-1: dfs(grid, (x+1, y))
            if y < len(grid[0])-1: dfs(grid, (x, y+1))

        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, (i, j))
                    numIslands += 1

        return numIslands
            