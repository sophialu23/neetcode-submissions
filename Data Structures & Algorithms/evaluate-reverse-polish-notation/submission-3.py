class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # step 1, 2: edge cases and constraints 
        # token length is always >= 1 
        
        # step 3: brute force, two for loops 
        # always try and find the operand and compute it between the two numbers in front of it 

        # step 4: solution > stack 
        # add all numbers into a stack
        # as soon as you see an operand, compute the numbers in that stack 
        # using that operand 
        # pop the two numbers, compute the answer, push the answer into the stack 
        # return the final number given in the stack 

        answer = [] 

        for s in tokens: 
            if s not in "+-*/": 
                answer.append(int(s))
            elif s == "+": 
                a = answer.pop()
                b = answer.pop()
                answer.append(a+b)
            elif s == "-": 
                a = answer.pop()
                b = answer.pop()
                answer.append(b-a)
            elif s == "*": 
                a = answer.pop()
                b = answer.pop()
                answer.append(a*b)
            else: 
                a = answer.pop()
                b = answer.pop()
                answer.append(int(b/a))
        
        return answer[-1]