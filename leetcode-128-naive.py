class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        count = 1
        maxcount = min(1,len(nums))
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] +1:
                count +=1
                maxcount = max(count,maxcount)
            elif nums[i] == nums[i-1]:
                pass
            else: count =1
        return maxcount