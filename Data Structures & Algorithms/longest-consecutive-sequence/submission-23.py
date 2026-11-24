class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxL = 0
        numSet = set(nums)

        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                maxL = max(length, maxL)
        
        return maxL