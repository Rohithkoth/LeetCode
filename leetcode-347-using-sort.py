class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i]+= 1
            else:
                count[i] =1
        
        zipped = list(zip(count.values(),count.keys()))
        print(zipped)
        zipped.sort()
        print(zipped)
        freq = [item[1] for item in zipped]
        return freq[-k:]