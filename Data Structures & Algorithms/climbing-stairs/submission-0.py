class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1 + self.climbStairs(n - 1)

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)