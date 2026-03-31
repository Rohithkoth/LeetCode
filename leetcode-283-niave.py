class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prodnz = 1
        out = [0]*len(nums)

        for i in nums:
            if i == 0:
                if prod == 0:
                    return out
                prodnz = prod
                prod = 0
            else:
                prod *= i
                prodnz *= i
        

        if prod == 0:
            for j in range(len(nums)):
                if nums[j] == 0:
                    out[j] = prodnz
        else:
            for j in range(len(nums)):
                out[j] = int(prod/nums[j])
        
        return out
            