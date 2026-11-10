class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        good = max(piles)

        while l <= r:
            mid = (l + r) // 2

            time = 0
            for i in piles:
                time += math.ceil(i / mid)
            if time <= h:
                good = mid
                r = mid - 1
            elif time > h:
                l = mid + 1
            
        return good