class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we are finding uniqueness here
        #we can use a hashset for uniqueness and check are you in the hashset
        #define hashset
        #for x in nums
        #if x not in nums x add else:
        #else return false
        #return true
        unique = set()
        for num in nums:
            if num in unique:
                return True
            else:
                unique.add(num)
        return False

        