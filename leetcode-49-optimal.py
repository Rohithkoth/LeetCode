class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countout = defaultdict(list)
        for s in strs:
            charcount = [0]*26
            for c in s:
                charcount[ord(c.lower())-ord("a")] +=1
            countout[tuple(charcount)].append(s)
        return list(countout.values())