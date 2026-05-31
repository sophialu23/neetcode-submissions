class Solution:
    def isValid(self, s: str) -> bool:
        # initialize the values that are paired together in a stack 
        parent_map = {')' : '(', ']' : '[', '}': '{'}
        # initialize the stack in python
        stack = []

        # stack uses append 
        for char in s: 
            # if the characters in parent map exist
            if char in parent_map.values(): 
                # add values to the stack 
                stack.append(char) 
            # if the characters is a closing bracket and exist within parent map 
            elif char in parent_map: 
                # if the stack is empty or the character is not inside parent open
                # bracket does not match the ending bracket 
                if not stack or stack[-1] != parent_map[char]: 
                    return False
                # if it passes this condition, pop the open and close bracket from the stack
                stack.pop()
        # return the stack if it is empty 
        # return false if the stack is not empty 
        return not stack 
        
      