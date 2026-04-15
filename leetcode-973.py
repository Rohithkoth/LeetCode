class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            dist = math.sqrt(i[0]**2+i[1]**2)
            distances.append([dist,i[0],i[1]])
        print(distances)
        heapq.heapify(distances)

        out = []

        for _ in range(k):
            p = heapq.heappop(distances)
            out.append([p[1],p[2]])
        
        return out