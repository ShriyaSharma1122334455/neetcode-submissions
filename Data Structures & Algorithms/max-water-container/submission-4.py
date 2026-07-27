class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0
        r = len(heights)-1
        finalarea =0
        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            finalarea = max(finalarea,area)
            if heights[l] <= heights[r]:
                l+=1
            else: 
                r-=1
            # if heights[l]<=heights[r]:
            #     area = heights[l]*(r-l)
            #     l+=1
            #     finalarea = max(finalarea,area)
            # if heights[l]>heights[r]:
            #     area = heights[r]*(r-l)
            #     r-=1
            #     finalarea = max(finalarea,area)
        return finalarea 
