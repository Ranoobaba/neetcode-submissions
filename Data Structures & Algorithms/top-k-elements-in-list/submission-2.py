from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        count = {}
        for numbers in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num in count.keys():
            heapq.heappush(min_heap, (count[num], num))
            if len(heap) > k:
                heapq.heapoppop(heap)

        storage = []
        for i in range(k):
            storage.append(heaqp.heappop(heap)[1])
        return storage



