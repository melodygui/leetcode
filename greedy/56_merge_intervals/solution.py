class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        intervals.sort(key = lambda i: i[0]) # sort by start times 

        merged = [intervals[0]] # add first interval to output

        for start, end in intervals[1:]: # iterate from second interval onwards
            lastEnd = merged[-1][1]
            if start <= lastEnd: # if there is overlap (curr start time on or before prev finish time)
                merged[-1][1] = max(lastEnd, end)
            else:
                merged.append([start, end])

        return merged 