class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # step 1, 2: edge cases and constraints 
        # m >= 1, n >= 1 

        # step 3: brute force strategy > for loop 
        # have a for loop and loop through all values in the matrix 

        # step 4: solution > binary search 
        # have a pointer at each side of the subarray 
        # check if the value is in between those numbers if so 
        # binary search, if not continue moving onto next 

        rows, cols = len(matrix), len(matrix[0])

        top = 0 
        bottom = rows - 1 

        while top <= bottom: 
            current_row = (top + bottom) // 2 # integer division
            if target > matrix[current_row][-1]: 
                top = current_row + 1 
            elif target < matrix[current_row][0]: 
                bottom = current_row - 1 
            else: 
                break 

        if not top <= bottom: 
            return False 
        current_row = (top + bottom) // 2 
        left, right = 0, cols-1 
        while left <= right: 
            middle = (left + right) // 2
            if target > matrix[current_row][middle]: 
                left = middle + 1 
            elif target < matrix[current_row][middle]: 
                right = middle - 1 
            else: 
                return True 

        return False 

