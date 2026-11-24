class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        numSet = set(nums)
        seen = set()

        for n in numSet:
            currMax = 0
            if n not in seen:
                while n+1 in numSet:
                    seen.add(n+1)
                    n += 1
                    currMax += 1
            
            seen.add(n)
            maxL = max(currMax+1, maxL)
        
        return maxL