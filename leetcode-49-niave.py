class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = defaultdict(list)
        for i in strs:
            sortedS = str(sorted(i))
            # if sortedS not in mapping:
            #     mapping[sortedS] = [i]
            # else:
            mapping[sortedS].append(i)
        
        listout = []

        for k in mapping.keys():
            listout.append(mapping[k])

        return listout