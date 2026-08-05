from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #so the index is 1 index so add 1 to the value of all the index at the very end
        #im getting in a list of numbers and return a list of numebers two numbers that are index [ 1 ,2 ]
        # we want to find a the values that equal this target value 
        #so im thinking I can use a hashmap i put all the values in a hashmap and then if I do a for loop and check if the value of the target - curr in values return the value of the index
        #the index should be in the key and the actual value of the number should be in values
        my_hashmap = defaultdict(int)
        result = []
        for i in range(len(numbers)):
            if target - numbers[i] in my_hashmap:
                return [my_hashmap[target - numbers[i]] + 1 , i + 1]
            my_hashmap[numbers[i]] = i
        


        