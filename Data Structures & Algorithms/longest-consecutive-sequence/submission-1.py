class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        result = 0 
        for num in nums:
            if num - 1 not in my_set:
                curr = 1
                while num + curr in my_set:
                    curr += 1
                result = max(curr,result)
        return result 

        