class Solution:
    def maxArea(self, heights: List[int]) -> int:
    #    areas = []
    #    for i in range(len(heights)):
    #        for j in range(i+1, len(heights)):
    #            areas.append(min(heights[i], heights[j]) * (j - i))
    #    return max(areas)
        areas = []
        i = 0
        j = len(heights) - 1
        #for _ in range(len(heights)):
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