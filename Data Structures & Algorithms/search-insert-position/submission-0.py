from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        # Use <= so we check the very last remaining element when l == r
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m  # Target found, return index immediately
                
            elif nums[m] < target:
                l = m + 1  # Target is to the right
                
            else:
                r = m - 1  # Target is to the left
                
        # If the target is not found, 'l' will naturally point 
        # to the correct index where it should be inserted.
        return l
