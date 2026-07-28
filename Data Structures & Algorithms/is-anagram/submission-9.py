
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap_s,hashmap_t = {}, {}
        for letter in s:
            hashmap_s[s[letter]] = hashmap.get(s[letter],0)
            hashmap_t[t[letter]] = hashmap.get(t[letter], 0)
            if hashmap_s == hashmap_t:
                return True
        return False
      
        

