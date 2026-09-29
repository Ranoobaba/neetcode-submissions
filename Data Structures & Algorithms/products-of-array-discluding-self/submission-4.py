class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if nums[j] == nums[i]:
                    if nums[j] == 0:
                        continue
                    else:
                        curr // nums[j]
                else:
                    curr *= nums[j]
            res.append(curr)
        return res 

        