class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):

            if prices[buy]<prices[sell]:#if i sell it for more than i bought it
                profit = prices[sell]-prices[buy]
                maxProfit = max(profit, maxProfit)
            else:
                buy = sell #if the sell price is better than what buy then let's buy on that day instead
            sell +=1

        return maxProfit
            