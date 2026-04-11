import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            k = self.total_hours(piles,mid)
            if k <= h:
                high = mid-1
            else:
                low = mid+1
        return low

    def total_hours(self,piles,k):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/k)
        return total_hours
        