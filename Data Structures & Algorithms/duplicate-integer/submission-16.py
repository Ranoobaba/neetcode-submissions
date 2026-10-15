class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set(nums)
        for num in nums:
            if num in check:
                return True
        return False
        