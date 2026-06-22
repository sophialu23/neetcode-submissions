class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # step 1, 2: edge cases and constraints 
        # temperatures length is always >=1 
        
        # step 3: brute force solution > double for loop
        # going through the array and checking till you find the greater value for each i 

        # step 4: solution > stack 
        # add all values to the array 
        # before adding, check if the added value is greater than the value at the bottom of the stack 
        # if it is then minus that values index, from the bottom one 
        # append it into your answer array 
        # and pop the bottom of the stack 
        # time complexity O(n), space complexity O(n)

        # append is add to the top, insert is add to the bottom 
        # pop is remove from top, pop(0) is remove from bottom O(n)
        stack = []
        answer = [0] * len(temperatures)
        
        # review 
        for i in range(len(temperatures)): 
            while stack and temperatures[i] > temperatures[stack[-1]]: 
                bigger = stack.pop() 
                answer[bigger] = i - bigger 
            stack.append(i)

        return answer 
