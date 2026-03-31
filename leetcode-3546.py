class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        sumto = 0
        for i in grid:
            sumto += sum(i)
        
        rowsum=0
        for j in grid:
            rowsum += sum(j)
            if rowsum == sumto/2:
                return True

        colsum = 0
        for m in range(len(grid[0])):
            for n in range(len(grid)):
                colsum += grid[n][m]
            if colsum == sumto/2:
                return True
        print(sumto)

        return False