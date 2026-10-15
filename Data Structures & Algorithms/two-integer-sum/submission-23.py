class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            nums_dict[i] = nums[i]
        for i in range (len(nums)):
            if target - nums[i] in nums_dict:
                for k,v in nums_dict.items():
                    if v == target - nums[i]:
                        return [i,k]
        

        