class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                if nums[j] == (target - nums[i]):
                    return [i,j]

        