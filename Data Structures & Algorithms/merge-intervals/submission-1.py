class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        i = 1
        while i <= len(intervals)-1:
            prev_start, prev_end = intervals[i-1]
            cur_start, cur_end = intervals[i]

            if cur_start <= prev_end:
                intervals[i][0] = prev_start
                intervals[i][1] = max(prev_end, cur_end)
                del intervals[i-1]
            else:
                i+=1
            
        return intervals