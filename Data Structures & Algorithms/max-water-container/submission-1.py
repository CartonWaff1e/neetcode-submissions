class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0
        while left < right :
            current = min(heights[left], heights[right]) * (right - left)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            area = max(area, current)
            current = area
        return area
