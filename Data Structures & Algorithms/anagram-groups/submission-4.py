from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        for word in strs:
            sw = "".join(sorted(word))
            s[sw].append(word)
        return list(s.values())