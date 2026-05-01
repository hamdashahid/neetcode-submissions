class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l,r = 0,len(height)-1
        maxL , maxR = height[l] , height[r]
        res = 0

        while l<r:
            if height[l] < height[r]:
                l+=1     # move right
                maxL = max(maxL,height[l]) # update max left
                res+= maxL - height[l]   # amunt of water
                
            else:
                r-=1      # move left
                maxR = max(maxR,height[r])
                res+= maxR - height[r]
        return res