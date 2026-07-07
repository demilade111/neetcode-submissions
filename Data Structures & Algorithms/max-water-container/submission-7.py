class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l],heights[r]) 
            width = r - l 
            waterarea = height * width 
            maxarea = max(waterarea,maxarea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea
              









        

