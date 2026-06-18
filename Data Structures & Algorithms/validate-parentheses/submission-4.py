class Solution:
    def isValid(self, s: str) -> bool:
        # step 1, 2: edge cases and constraints 
        # length of s could be = 1 
        # if s is odd, cannot be true 

        if len(s) == 1: 
            return False 
        
        if len(s) % 2 != 0: 
            return False 

        # step 3: brute force > for loops finding every match 

        # step 4: solution > stack 
        # create a parent map to coordinate which parathenses are together 
        # add all characters to stack 
        # if the top matches parent map > pop
        # check if stack is empty at the end 
        
        stack = []
        # this is a dictionary 
        # key : value 
        map_c = {")": "(", "]": "[", "}": "{"}    

        # i is the value 
        for i in s: 
            if i in map_c: 
                # if stack is not empty and it has a matching open bracket
                if stack and stack[-1] == map_c[i]:
                    # pop the open bracket
                    stack.pop()
                # if it does not have a matching one return False 
                else: 
                    return False 
            # if its an open bracket append 
            else: 
                stack.append(i)

        # return true when stack is empty 
        return not stack 

             
        
      