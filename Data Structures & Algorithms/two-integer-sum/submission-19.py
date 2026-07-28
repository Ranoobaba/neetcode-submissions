class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storagemap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in storagemap:
                return [storagemap[diff], i]
            storagemap[n] = i
    


        