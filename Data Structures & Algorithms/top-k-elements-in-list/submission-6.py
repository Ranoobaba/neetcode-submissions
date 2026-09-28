from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = []
        storage = defaultdict(list)
        for i in range(len(nums)):
            storage[nums[i]].append(0)
        while k > 0:
            res = max(storage, key=lambda k:len(storage[k]))
            final.append(res)
            del storage[res]
            k -= 1
        return final


    
        


