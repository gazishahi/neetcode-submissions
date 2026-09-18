class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxL = 0
        currL = 0

        for n in nums:
            if n == 1:
                currL += 1
            else:
                currL = 0
            
            maxL = max(maxL, currL)
        
        return maxL