class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r: #since they are sorted we are checking to see if there is a match using 2 pointers
            if numbers[l]+numbers[r]  == target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]  > target:#shift direction based on whether we are greater than or less than the target
                r-=1
            elif numbers[l]+numbers[r]  < target:
                l+=1
        
        
            