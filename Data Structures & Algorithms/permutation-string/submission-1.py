class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #we can just use in s1
        if not s2 or not s1:
            return False


            #if the length of the window == len(s1):
            #return true
        l = 0
        r = 0
        res = ""
        while l <= r and r < len(s2):
            if s2[r] not in s1:
                r += 1
            elif s2[r] in s1 and len(res) == 0:
                l = r
                res += s2[r]
                r += 1
            else:
                res += s2[r]
                r += 1
                print(res)
        new,news1 = sorted(res),sorted(s1)
        new,news1 =  "".join(new),"".join(news1)
        if new == news1:
            return True
        else:
            return False
        

            



        