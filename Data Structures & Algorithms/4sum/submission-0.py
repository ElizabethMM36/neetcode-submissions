from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        
        def kSum(k: int, start: int, target: int):
            # Base Case: Use two-pointer approach when k == 2
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    current_sum = nums[l] + nums[r]
                    if current_sum < target:
                        l += 1
                    elif current_sum > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                return

            # Recursive Case: Reduce k-Sum down to (k-1)-Sum
            for i in range(start, len(nums) - k + 1):
                # Skip duplicate elements to avoid duplicate quadruplets
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res
