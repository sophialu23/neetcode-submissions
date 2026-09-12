class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # this solution is O(1)
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False # this is the overlapping first spot 

        # determine which rows and cols need to be 0 
        for r in range(rows): 
            for c in range(cols): 
                if matrix[r][c] == 0: 
                    matrix[0][c] = 0 
                    if r > 0: # we cant set that top left position 
                        matrix[r][0] = 0 
                    else: 
                        row_zero = True 

        for r in range(1, rows): 
            for c in range(1, cols): 
                if matrix[0][c] == 0 or matrix[r][0] == 0: 
                    matrix[r][c] = 0 

        if matrix[0][0] == 0: 
            for r in range(rows): 
                matrix[r][0] = 0 
        if row_zero == True: 
            for c in range(cols): 
                matrix[0][c] = 0 


        