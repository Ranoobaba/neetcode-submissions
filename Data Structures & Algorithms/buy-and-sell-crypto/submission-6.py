class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input is an array of prices, output is max(prices[i]- prices[j])
        #naive solution would be to iterate through the entire list with two indexs, and calulate the max value which would be on O(N^2)
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
               sellprice, buyprice = prices[j], prices[i]
               profit = sellprice - buyprice
               max_profit = max(max_profit, profit)
        return max_profit



        