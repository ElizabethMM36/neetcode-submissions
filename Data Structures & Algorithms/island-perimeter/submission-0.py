from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()

        def dfs(i, j):
            # Base Case 1: If out of bounds or hitting water, it's a perimeter edge
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 1
            
            # Base Case 2: If already visited land, it contributes 0 to perimeter
            if (i, j) in visit:
                return 0
            
            # Mark as visited (Note the double parentheses for the tuple)
            visit.add((i, j))
            
            # Sum up perimeter from all 4 directions
            perim = dfs(i, j + 1)
            perim += dfs(i + 1, j)
            perim += dfs(i, j - 1)
            perim += dfs(i - 1, j)
            
            return perim

        # Find the first piece of land and start DFS
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
                    
        return 0