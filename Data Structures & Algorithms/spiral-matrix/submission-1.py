class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # step 1: edge cases and constraints always going to at least have one value 
        
        # step 2: clarifying questions 
        
        # step 3: solution 
        # traverse the table and add 
        result = [] 
        # time complexity is O(m*n) 
        left = 0 
        right = len(matrix[0])
        top = 0 
        bottom = len(matrix)

        while left < right and top < bottom: 
            # left to right and get every value in top value 
            for i in range(left, right): 
                result.append(matrix[top][i])
            top += 1 
            for i in range(top, bottom): 
                result.append(matrix[i][right-1])
            right -= 1 
            # we must check inbetween because the while loop only checks after all these fors are done 
            # what if in the case of one row or one column 
            if top < bottom: 
                for i in range(right - 1, left - 1, -1): #python is not, -inclusive, -1 means reverse 
                    result.append(matrix[bottom-1][i])
                bottom -= 1
            if left < right: 
                for i in range(bottom -1, top -1, -1): 
                    result.append(matrix[i][left])
                left += 1 
        return result 


