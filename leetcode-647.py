class Solution:
    def countSubstrings(self, s: str) -> int:
        
        outs = set()

        for i in range(len(s)):
            l=i
            r=i
            # print(i)
            while l>=0 and r<len(s) and s[l] == s[r]:
                # print(l,r)
                outs.add((l,r))
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                # print(l,r)
                outs.add((l,r))
                l-=1
                r+=1
        # print(outs)
        return len(outs)
