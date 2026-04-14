class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mind = 2**31

        for i in range(len(nums)):
            if target == nums[i]:
                mind = min(abs(i-start), mind)
        
        
        return mind