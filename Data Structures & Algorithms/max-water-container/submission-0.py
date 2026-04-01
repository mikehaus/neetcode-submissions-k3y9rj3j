# The area is pegged to whatever the lower edge is
# need to multiply l x min(h) to get area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1
        ogR = len(heights) - 1
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            res = max(cur, res)
            if r == l + 1:
                l += 1
                r = ogR
            else:
                r -= 1
        return res