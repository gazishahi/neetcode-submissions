class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check rows
        # check cols

        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            midR = (top + bot) // 2

            if matrix[midR][0] > target:
                bot = midR - 1
            elif matrix[midR][COLS-1] < target:
                top = midR + 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        finR = (top + bot) // 2
        left, right = 0, COLS - 1
        
        while left <= right:
            midC = (right + left) // 2

            if matrix[finR][midC] > target:
                right = midC - 1
            elif matrix[finR][midC] < target:
                left = midC + 1
            else:
                break

        finC = (left + right) // 2
        return matrix[finR][finC] == target