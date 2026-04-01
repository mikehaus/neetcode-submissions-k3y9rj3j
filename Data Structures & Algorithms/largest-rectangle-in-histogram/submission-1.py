class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]

        # The largest area is composed of a bunch of smaller rectangles
        # The trick here is to keep track of the min height for a window and then multiply by width
        # width for a window is r - l
        # The max value is max(1 * h, minH * (r - l))
        # We need to compare at each subwindow 
        for l in range(len(heights)):
            r = l + 1
            if r == len(heights):
                break
            minL, minR = heights[l], heights[r]
            while r < len(heights):
                width = r - l
                minR = min(minR, heights[r])
                left = heights[l]
                right = heights[r]
                res = max(res, left, right, min(minL, minR) * (r - l + 1))
                r += 1
            l += 1
        return res
            