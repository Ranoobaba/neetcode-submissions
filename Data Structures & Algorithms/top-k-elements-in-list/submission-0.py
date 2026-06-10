from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        result = []

        # Count the frequency of each number
        for num in nums:
            hashmap[num] += 1

        # Get the top k frequent elements
        while k != 0:
            top = max(hashmap, key=hashmap.get)
            result.append(top)
            del hashmap[top]
            k -= 1

        return result

