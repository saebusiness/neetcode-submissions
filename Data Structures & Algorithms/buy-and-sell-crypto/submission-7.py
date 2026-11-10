class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_p = 0
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l = i
            p = prices[i] - prices[l]
            max_p = max(max_p,p)
        return max_p
