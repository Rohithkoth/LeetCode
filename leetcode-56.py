class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #sorting is key here
        i=1
        print(intervals)
        while i < len(intervals): #this is how we merge the intervals, same principle for all intervals problems
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1] = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i][1], intervals[i-1][1])]
                intervals = intervals[:i] + intervals[i+1:]
            else:
                i+=1
        return intervals