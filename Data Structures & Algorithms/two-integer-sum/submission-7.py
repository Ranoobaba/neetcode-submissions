class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,number in enumerate(nums):
            difference = target - number
            if difference in seen:
                return [seen[difference],i]
            seen[number] = i
            
             

        
        