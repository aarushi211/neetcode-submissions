class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights) - 1
        while j>i:
           area = (j-i) * min(heights[j], heights[i])
           res = max(res, area) 
           if heights[j]<heights[i]: 
            j -= 1
           else: 
            i += 1
        return res