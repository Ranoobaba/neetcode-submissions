from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        count = {}
        for numbers in nums:
            count[numbers] = 1 + count.get(numbers, 0)
        
        for num in count.keys():
            heapq.heappush(min_heap, (count[num], num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        storage = []
        for i in range(k):
            storage.append(heapq.heappop(min_heap)[1])
        return storage



