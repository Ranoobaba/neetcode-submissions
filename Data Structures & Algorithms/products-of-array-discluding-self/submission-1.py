class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #so we get a list of nums and we need to return a list of nums such that the nums[0] == result[0] == nums[i+1:length] * each other 
        #use a set to see the number that we are multiplying 
        #then use i and j format where j always starts at 1
        #i is the pointer that is showing us the current index and what to check in teh set and what when j == i to ignore and J ++ 1 
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            print(res[i],prefix)
            res[i] = prefix
            prefix *= nums[i]
            print(prefix)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        



        