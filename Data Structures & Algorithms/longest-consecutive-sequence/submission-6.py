
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        top_curr = 0
        curr = 0
        for num in nums:
            while num -1 in nums:
                if num - 1 not in nums:
                    curr = 1
                else:
                    curr += 1
                top_curr = max(top_curr, curr)
        return top_curr

        