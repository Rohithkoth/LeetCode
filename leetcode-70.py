class Solution:
    def climbStairs(self, n: int) -> int:
        
        stairs = [0 for i in range(n)]
        if len(stairs)>=1:
            stairs[-1] = 1
        if len(stairs)>=2:
            stairs[-2] = 2
        for j in range(len(stairs)-3,-1,-1):
            # if j+2<len(stairs):
            stairs[j] += stairs[j+2]
            stairs[j] += stairs[j+1]
        print(stairs)
        return stairs[0]