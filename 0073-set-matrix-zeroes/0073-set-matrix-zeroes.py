class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_zero = set()
        col_zero = set()
        # Find rows and cols to convert
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    row_zero.add(row)
                    col_zero.add(col)
        
        # Change up rows
        for row in row_zero:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        # Change up columns
        for col in col_zero:
            for row in range(len(matrix)):
                matrix[row][col] = 0

        return matrix
