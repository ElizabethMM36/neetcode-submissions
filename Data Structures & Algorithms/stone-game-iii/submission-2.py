from typing import List

class Solution:
    def stoneGameIII(self, values: List[int]) -> str:
        n = len(values)
        
        # dp[i] represents the max relative score difference starting from index i.
        # We only need 3 states to look ahead: i+1, i+2, and i+3.
        # Base cases: past the end of the array (indices n, n+1, n+2), the score diff is 0.
        dp = [0] * 3 
        
        # Process from right to left
        for i in range(n - 1, -1, -1):
            res = float("-inf")
            running_sum = 0
            
            # Try taking 1, 2, or 3 stones
            for j in range(i, min(i + 3, n)):
                running_sum += values[j]
                # dp[(j + 1) % 3] gives us the pre-computed opponent's best score diff
                res = max(res, running_sum - dp[(j + 1) % 3])
            
            # Store current result in dp[i % 3] to update the sliding window
            dp[i % 3] = res
            
        # The final result starting from index 0
        score_diff = dp[0]
        
        return "Alice" if score_diff > 0 else ("Bob" if score_diff < 0 else "Tie")