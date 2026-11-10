class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        r = piles[-1]
        speed = r

        while l <= r:
            k = (l + r) // 2
            
            hours = 0
            for i in piles:
                hours += math.ceil(float(i) / k) 
            
            if hours <= h:
                r = k - 1
                speed = k
            else:
                l = k + 1
            
            
            
        return speed