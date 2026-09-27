class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # track longest
        # when we reach a number, we check if its prev num exists
        # if not, then we start from that number and see if the next numbers appear
        # track the longest amount we can get until we traverse thru the whole array

        numSet = set(nums)
        trackL = 0
        maxL = 0

        for n in numSet:
            if n-1 not in numSet:
                while n+1 in numSet:
                    trackL += 1
                    n += 1
            
            maxL = max(trackL+1, maxL)
            trackL = 0

        return maxL