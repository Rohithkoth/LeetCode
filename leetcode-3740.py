import sys

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        vals = {}
        for i in range(len(nums)):
            if nums[i] not in vals:
                vals[nums[i]] = []
            vals[nums[i]].append(i)

        mind = 2**31-1
        print(vals)
        for j in (vals.values()):
            if len(j) >= 3:
                for k in range(1,len(j)-1):
                    mind = min(mind, abs(j[k-1]-j[k]) + abs(j[k]-j[k+1]) + abs(j[k+1] - j[k-1]) )


        if mind != 2**31-1:
            return mind
        return -1