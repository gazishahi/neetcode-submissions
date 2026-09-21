class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # store nums into set
        # as we traverse thru the set, we continue checking if the next num in set
        # while loop to keep checking, break if no longer there
        # update max from that while loop
        # [0,3,2,5,4,6,1,1]
        # numSet = [0,3,2,5,4,6,1]
        # 

        # if n+1 in set
        # increment max
        


        numSet = set(nums)
        maxL = 0
        currMax = 0

        if not nums:
            return 0

        for n in numSet:
            if n-1 not in numSet:
                currMax = 1
                i = n
                while i+1 in numSet:
                    currMax += 1
                    i += 1
            
            maxL = max(maxL, currMax)
        
        return maxL