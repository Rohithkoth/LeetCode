class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry =1
        for i in range(len(digits)-1,-1,-1):
            # if digits[i] + carry>=10:
            temp = (digits[i] + carry)%10
            carry = (digits[i] + carry)//10
            digits[i] = temp
            print(carry)
        if carry == 1:
            return [1] + digits
        return digits