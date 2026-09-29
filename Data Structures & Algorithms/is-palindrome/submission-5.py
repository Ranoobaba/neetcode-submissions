class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for char in s:
            if char.isalnum():
                new += char.lower()  
        left = 0
        right = len(new)- 1
        while right >= left:
            if new[right] != new[left]:
                return False
            else:
                right -= 1
                left += 1
        return True
           
       