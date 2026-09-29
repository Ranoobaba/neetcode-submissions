from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so we cant use a sorting function since thats in nlogn but what we can do 
        numbers = set(nums)
        res = 1
        curr = 1
        for num in nums:
            while num + 1 in numbers:
                    curr += 1
                    num += 1
            else:
                res = max(curr,res)
                curr = 1
        return res
        
        