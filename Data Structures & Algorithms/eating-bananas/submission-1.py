import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ##this can be solved using a binary search
        low = 1
        high = max(piles)
        k = 0
        while low <= high:
            mid = (low+high)//2
            ans = 0
            for i in range(len(piles)):
                ans += math.ceil(piles[i]/mid)
            if ans <= h:
                k = mid
                high = mid - 1
            else:
                low = mid + 1
        return k



                
        