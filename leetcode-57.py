class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)<1 or intervals[-1][0]<newInterval[0]:
            intervals.append(newInterval)

        elif intervals[0][0] >= newInterval[0]:
            intervals = [newInterval] + intervals
        
        else:
            for i in range(1,len(intervals)):
                if newInterval[0]>= intervals[i-1][0] and newInterval[0]<=intervals[i][0]:
                    intervals = intervals[:i] + [newInterval] + intervals[i:]

        i=1
        print(intervals)
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1] = [min(intervals[i-1][0], intervals[i][0]), max(intervals[i][1], intervals[i-1][1])]
                intervals = intervals[:i] + intervals[i+1:]
            else:
                i+=1
        return intervals
    
    #while this is an O(n) solution the nlogn is not much better becuase it is only inserting one of the elements
    #and the rest of the code is largely the same when it comes to mergint the intervals
    