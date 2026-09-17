class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while idx and curr > temperatures[idx[-1]]:
                result[idx[-1]] = i - idx[-1]
                idx.pop()
            idx.append(i)

        
        return result