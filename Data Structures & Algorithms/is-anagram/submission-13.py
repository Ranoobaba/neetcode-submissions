
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = set()
        seen_t = set()
        for letters in s:
            seen_s.add(letters)
        for letters in t:
            seen_t.add(letters)
        if seen_t == seen_s:
            return True
        return False



      
        

