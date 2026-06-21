class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # implementing a cache using a hashmap key = (i , buying)
        def dfs(i , buying):
            if i >= len(prices):
                return 0
            # if it is already in the hashmap then the price is already stored
            if (i, buying) in dp:
                return dp[(i,buying)]
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown= dfs(i + 1 , buying)
                dp[(i,buying)] = max(buy, cooldown)
 
            else:
                sell = dfs(i + 2 , not buying) + prices[i]
                cooldown= dfs(i + 1 , buying)
                dp[(i,buying)] = max(sell, cooldown)
            return dp[(i,buying)]
        return dfs(0, True)
 


            

        