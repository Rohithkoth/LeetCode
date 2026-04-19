class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x,y):
            if x<len(grid[0]) and x>=0 and y<len(grid) and y>=0:
                if grid[y][x] == "1":
                    grid[y][x] = "2"
                    dfs(x+1,y)
                    dfs(x-1,y)
                    dfs(x,y+1)
                    dfs(x,y-1)
            return
        count =0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count+=1
                    dfs(c,r)

        return count
