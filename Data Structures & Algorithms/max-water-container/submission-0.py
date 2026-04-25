class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # i,0 & i,height[i] => forms first line
        # j,0 & j,height[j] => forms second line
        # area = length * width 
        # length = j-i
        # width =min(height[j] , height[i]) 
        max_area =0 
        n = len(heights)
        i=1
        j=n

        while(i<j):
            length = abs(j-i)
            width = min(heights[j-1], heights[i-1])
            area = length * width
            max_area = max(max_area,area)

            if heights[i-1]<heights[j-1]:
                i+=1
            elif heights[i-1]>heights[j-1]:
                j-=1
            else:
                i+=1


        return max_area
 