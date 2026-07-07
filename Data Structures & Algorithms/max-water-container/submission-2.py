class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height = min(heights[i],heights[j]) //1
                width = j - i 
                waterarea = height * width 
                maxarea = max(waterarea,maxarea)
        return maxarea
              









        

