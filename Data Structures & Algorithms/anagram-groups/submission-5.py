from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = defaultdict(list)
        count = [0] * 26
        for word in strs:
            for c in word:
                count[ord('a') - ord(c)] += 1
            s[tuple(count)].append(word)
            count = [0] * 26
        return list(s.values())
            
