class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for char in s:
            if char.isalnum() == True and char != ' ':
                new_s += char.lower()
        l = 0
        r = len(new_s) -1 
        while l < r:
            if new_s[r] != new_s[l]:
                return False
            else:
                l += 1
                r -= 1
        return True

        