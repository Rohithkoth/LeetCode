class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [0 for i in range(len(cost))]
        if len(cost)<=2:
            return min(cost[-1],(cost[-2]))

        mincost[-1] =cost[-1]
        mincost[-2] = cost[-2]
        for j in range(len(cost)-3,-1,-1):
            mincost[j] = cost[j] + min(mincost[j+1],mincost[j+2])
        print(mincost)
        return min(mincost[0],mincost[1])