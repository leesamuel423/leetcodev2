class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      minimum = float("inf")
      max_profit = 0

      for i in prices:
        if i < minimum:
          minimum = i
        elif i - minimum > max_profit:
          max_profit = i - minimum
      
      return max_profit
        

"""

minimum = Infinity
maxProfit = -Infinity

iterate through prices
  if price < minimum: set minimum to prices
  if price - minimum > maxProfit: set maxProfit to difference

return maxProfit

"""