from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #we want to do nums[current] - target = value
       #if any other array in the nums statisfys that yes, return [current,index]
       #else i += 1
       # 4:0
       # 5:1
       # 6:2. the keys are the values of the array and the indexs are the values in the dictionary 
       seen = {}
       for i,x in enumerate(nums):
        value = target - x
        if value in seen:
            return [seen[value], i]
        seen[x] = i
             

        
        