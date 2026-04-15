class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        # length = 0
        maxlength = 0
        l=0
        r = 0
        while r<len(s):
            if s[r] not in chars:
                # length+=1
                pass
            else:
                while l < r:
                    chars.remove(s[l])
                    l+=1
                    if s[l-1] ==s[r]:
                        break
                    

            chars.add(s[r])
            r+=1
            # length = r-l
            print(chars)
            print(l,r)
            maxlength = max(maxlength, r-l)
            # print(length,maxlength)
        return maxlength