class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #what important is that i do the count of the length at the end of loop not at the start when we do the R check 
        if len(s) == 0:
            return 0
        else:
            l = 0
            r = 1
            sub = s[0]
            res = 1
            while (l <= r) & (r < len(s)):
                if s[r] in sub:
                    sub = s[l+1:r]
                    l += 1
                    r += 1
                else:
                    sub += s[r]
                    print(sub,len(sub))
                    r += 1
                    res = max(res,len(sub))
        return res
                

            