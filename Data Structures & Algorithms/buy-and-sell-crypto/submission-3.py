class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_p = 0

        for r in range(len(prices)):
            p = prices[r] - prices[l]
            if p < 0:
                l = r
            max_p = max(p,max_p)
        
        return max_p