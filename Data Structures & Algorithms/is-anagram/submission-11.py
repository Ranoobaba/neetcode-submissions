
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if sorted(s) == sorted(t):
         #   return True
        #return False
        map_s = {}
        map_t = {}
        for char in s:
            map_s[char] = map_s.get(char,0) + 1
        for char in t:
            map_t[char] = map_t.get(char,0) + 1
        if map_s == map_t:
            return True
        return False
       
      
        

