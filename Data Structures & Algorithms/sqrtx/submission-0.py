class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = self.mySqrt(x >> 2) << 1
        r = l + 1
        return l if r ** 2 > x else r
