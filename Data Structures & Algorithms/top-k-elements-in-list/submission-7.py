from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        # min-heap solution
        # min_heap = []

        # for num, count in freq.items():
        #     heapq.heappush(min_heap, (count, num))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        
        # return [num for count, num in min_heap]

        # (freq, number) 
        # keep track of size k

        # bucket-sort
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result


        