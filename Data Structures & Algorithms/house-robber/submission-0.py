class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0 , 0
        #then houses that are robbed
        #[rob1, rob2, n, n+1]
        for n in nums:
            # temp indicates the maximum house that can be robbed up until now
            temp= max(n + rob1 , rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
