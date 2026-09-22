class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top < bot:
            row = (top + bot) // 2

            if target > matrix[row][COLS-1]:
                top = row+1
            elif target < matrix[row][0]:
                bot = row
            else:
                break
        
        if (bot < top):
            return False
        
        row = (top + bot) // 2

        l, r = 0, COLS - 1

        while l < r:
            col = (l + r) // 2

            if target > matrix[row][col]:
                l = col + 1
            elif target < matrix[row][col]:
                r = col
            else:
                return True
        
        col = (l + r) // 2

        return matrix[row][col] == target