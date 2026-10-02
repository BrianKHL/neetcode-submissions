class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l = buy, r = sell

        l, r = 0,1
        maxProfit = 0

        while r < len(prices):
            #Check profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

