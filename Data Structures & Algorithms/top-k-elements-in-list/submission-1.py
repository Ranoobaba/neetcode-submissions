from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        for numbers in nums:
            heapq.heappush(max_heap, -numbers)
        storage = []
        seen = set()
        while k > 0:
            value = -heapq.heappop(max_heap)
            if value in seen:
                continue
            storage.append(value), seen.add(value)
            k -= 1 
        return storage
       
            



