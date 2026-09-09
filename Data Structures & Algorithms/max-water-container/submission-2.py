class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0

        while l < r:
            newA = min(heights[l], heights[r]) * (r - l)
            maxA = max(maxA, newA)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
                l += 1
            

        



        return maxA