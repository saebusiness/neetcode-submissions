class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0

        while l <= r:
            mid = (l + r) // 2
            time = 0

            for i in piles:
                time += math.ceil(i/mid)

            if time > h:
                print("The time was " + str(time) + " which is more than the hours, increasing search")
                l = mid + 1
            elif time <= h:
                print("The time was " + str(time) + " which is less than the hours, lowering search to find smaller number that works")
                k = mid
                r = mid - 1
            
        
        return k
        