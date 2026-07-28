
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = set()
        for letters in s:
            seen.add(letters)
        for letters in t:
            if letters not in seen:
                return False
        return True



      
        

