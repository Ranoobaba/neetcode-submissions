class Solution:
    def isValid(self, s: str) -> bool:
        left = 0
        right = len(s) -1 
        reverse = s[::-1]
        while left < right:
            print(s[left], reverse[right])
            if s[left] != reverse[right]:
                return False
            right -= 1
            left += 1
        return True
            
            

        