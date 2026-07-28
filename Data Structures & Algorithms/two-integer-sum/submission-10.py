from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       #we want to do nums[current] - target = value
       #if any other array in the nums statisfys that yes, return [current,index]
       #else i += 1
       count = 0
       new_nums = sorted(nums)
       for index in range(len(new_nums)):
        current = new_nums[index]
        searchvalue = target - current
        for j in range(len(new_nums[1:])):
            if new_nums[j] == current and new_nums[j] == searchvalue:
                return [index, j] 
            if new_nums[j] == searchvalue:
                return [index - count ,j + count]
        count +=  1


        
             

        
        