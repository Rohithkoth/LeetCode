class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            if x<len(grid[0]) and x>= 0 and y<len(grid) and y>=0:
                if grid[y][x] == 1:
                    grid[y][x] = 2
                    return 1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1)
            return 0

        currMax = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] ==1:
                    currMax = max(dfs(c,r), currMax)
        print(grid)
        return currMax