class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in List:
            copy = List[i+1:]
            for t in copy:
                if list[i] == copy[t]:
                    return true
                else:
                    t = t+1
            i = i+ 1
        return false
