class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get count of each n in num
        # fill freq array grouping numbers based on how many times they appear
        # iterate thru freq array backwards since the end of it would have the highest freqs
        # return the first k numbers
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for i, c in count.items():
            freq[c].append(i)
        
        for j in range(len(freq)-1, -1, -1):
            for m in freq[j]:
                if len(res) < k:
                    res.append(m)
        
        return res