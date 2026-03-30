class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: #suboptimal solution needs to use set
        if len(s) < 2:
            return len(s)

        l = 0
        r = 1
        
        count=0
        passed = {}
        passed[s[l]] = 1
        while r<len(s):
            if s[r] not in passed:
                count = max(count,r-l)
                passed[s[r]] =1
                r = r+1
            else:
                passed.pop(s[l])
                l = l+1
        return count+1
            