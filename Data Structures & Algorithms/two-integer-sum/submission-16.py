class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = sorted(nums)
        r = 0
        left = len(new_list) - 1
        while r < left:
            if nums[r] + nums[left] - target > 0:
                left -= 1
            elif nums[r] + nums[left] - target < 0:
                r += 1
            else:
                return [r,left]


        