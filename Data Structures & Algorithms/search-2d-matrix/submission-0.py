class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m * n) - 1

        while left <= right:
            middle = (left+right)//2
            row = middle // n
            col = middle % n
            mid_value = matrix[row][col]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = middle +1
            else:
                right = middle - 1
        return False



   