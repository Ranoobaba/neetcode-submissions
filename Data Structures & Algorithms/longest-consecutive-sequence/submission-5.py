from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so we cant use a sorting function since thats in nlogn but what we can do 
        numbers = set(nums)
        longest = 0
        if len(nums) == 0:
            return 0
        for num in numbers:
            if (num - 1) not in numbers:
                length = 1
                while (num + length) in numbers:
                    length += 1
                longest = max(length, longest)
        return longest 
        
        