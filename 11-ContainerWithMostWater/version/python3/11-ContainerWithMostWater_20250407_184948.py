# Last updated: 4/7/2025, 6:49:48 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1
        maxarea = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxarea = max(maxarea, area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return maxarea

        