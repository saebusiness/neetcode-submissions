class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2

            time = 0
            for i in piles:
                eat_time = math.ceil(float(i) / float(mid))
                time += eat_time

            if time <= h:
                good = mid
                r = mid - 1
            else:
                l = mid + 1
            
            
                
        return good