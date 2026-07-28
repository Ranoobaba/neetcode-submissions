class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = set()
        for n in s:
            hashset.add(n)
            for h in t:
                if h in hashset:
                    print(h)
                return False
        