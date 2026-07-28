class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()
        for n in s:
            hashset.add(n)
        for h in t:
            if h not in hashset:
                return False
        return True