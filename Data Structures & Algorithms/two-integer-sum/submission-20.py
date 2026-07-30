#one answer is definetely there
#so we want to use some math here.
#the basic solution would be loop within a loop so that would be o(n^2) for the time complexity can we do better?
#yes lets use a hashmap
#what are returning we are returning the index of a number , so I want to find the fastest way since I want to return the index and its faster to find the keys that he values in a hashmap the index should be in the key.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hashmap = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in my_hashmap.keys():
                return [my_hashmap[complement], i]
            my_hashmap[n] = i
        

        


        