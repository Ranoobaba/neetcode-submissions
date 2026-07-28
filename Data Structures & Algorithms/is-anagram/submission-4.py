class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()
        for n in s:
            hashset.add(n)
        if len(s) != len(t):
            return False
        for h in t:
            if h not in hashset:
                return False
        return True