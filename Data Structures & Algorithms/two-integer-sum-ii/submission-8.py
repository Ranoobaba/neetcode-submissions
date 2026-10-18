class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since i need to return a O(1) additional space complexity 
        #that means we need to iterate through the list without creating a new list, so we need to use a couple of pointers 
        l = 0  
        r = 1
        while l < r and r < len(numbers) - 1:
            total = numbers[l] + numbers[r] 
            if total == target:
                return list([l+1, r +1])
            elif total < target:
                r += 1
            else:
                l += 1
    
                






        