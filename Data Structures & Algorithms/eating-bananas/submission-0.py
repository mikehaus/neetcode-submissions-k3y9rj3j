class Solution:
    def getHours(self, piles: List[int], k: int) -> int:
        res = 0
        for p in piles:
            res += math.ceil(p / k)
        return res

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if self.getHours(piles, m) <= h:
                r = m
            else:
                l = m + 1
        return l