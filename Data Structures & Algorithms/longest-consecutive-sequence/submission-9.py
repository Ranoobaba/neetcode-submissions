class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        top_curr = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                curr = 1
                while num + curr in nums_set:
                    curr += 1
                top_curr = max(top_curr, curr)
        return top_curr

        