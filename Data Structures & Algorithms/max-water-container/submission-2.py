class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return 1 * min(heights[0], heights[1])
        l, r = 0, len(heights) - 1
        max_area = 0

        for l in range(len(heights) - 2):
            while r > l:
                area = (r - l) * min(heights[r], heights[l])
                if area > max_area:
                    max_area = area
                r -= 1
            
            r = len(heights) - 1
                
        return max_area