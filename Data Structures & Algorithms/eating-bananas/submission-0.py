class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)
        smallest = r
        while l <= r:
            middle = l + r // 2
            #the logic for calculation
            hours_taken = 0
            for pile in piles:
                if pile < middle:
                    hours_taken += 1
                elif pile % middle == 0:
                    hours_taken += pile // middle
                else:
                    while pile % middle != 0:
                        hours_taken += pile // middle
                        pile = pile - middle
                    hours_taken += 1
                

                
                if hours_taken > h:
                    l = middle + 1
                elif hours_taken <= h:
                    if middle < smallest:
                        smallest = middle
                    r = middle - 1
            return smallest








        