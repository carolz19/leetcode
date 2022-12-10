class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q1 = []
        q2 = []
        minutes = 0
			
        # find rotten oranges & add to q1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q1.append((i, j)) # add to q1
            
        # there are no rotten oranges and no fresh oranges
        if not q1 and not self.hasFreshOranges(grid): return 0
            
        while q1 or q2:
            # we've reached another minute
            if not q1:
                minutes += 1
                q1 = q2
                q2 = []
            
            # no more fresh oranges to check
            if not q1 and not q2: break
            
            curr = q1.pop(0) # get current node
            i,j = curr # the coordinates
            
            # add children to q2 and mark them as visited (grid = 2)
            if i > 0 and grid[i-1][j] == 1:
                q2.append((i-1, j))
                grid[i-1][j] = 2
            
            if i < len(grid) - 1 and grid[i+1][j] == 1:
                q2.append((i+1, j))
                grid[i+1][j] = 2
            
            if j > 0 and grid[i][j-1] == 1:
                q2.append((i, j-1))
                grid[i][j-1] = 2
            
            if j < len(grid[0])-1 and grid[i][j+1] == 1:
                q2.append((i, j+1))
                grid[i][j+1] = 2
      
        return -1 if self.hasFreshOranges(grid) else minutes

    def hasFreshOranges(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False