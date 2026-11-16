class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        i = 0
        j = len(heights) - 1
        while i != j and i < j:
            areas.append(min(heights[i], heights[j]) * (j - i))
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
                j -= 1
        return max(areas)