class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack to track the next hottest 
        # curr = 30
        # first while gets skipped since hottest is empty
        # hottest = [30]
        # curr = 38
        # while loops triggers since condition is met
        # result[0] = 1
        # hottest = []
        # hottest = [38]
        # curr = 30
        # hottest = [38, 30]
        # curr = 36
        # while loop triggers since condition is met


        idx = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while idx and curr > temperatures[idx[-1]]:
                result[idx[-1]] = i - idx[-1]
                idx.pop()
            idx.append(i)

        
        return result