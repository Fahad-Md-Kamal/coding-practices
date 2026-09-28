class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp, rp = 0, 1
        maxProfit = 0

        while rp < len(prices):
            if prices[rp] < prices[lp]:
                lp = rp
            else:
                profite = prices[rp] - prices[lp]
                maxProfit = max(profite, maxProfit)
            rp += 1
        return maxProfit
