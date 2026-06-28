class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0
        for i in nums:
            count[i] += 1
            if maxCount < count[i]:
                res = i 
                maxCount = count[i]
        return res

            
        