class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # step 1, 2: edge cases and constraints 
        # length of heights >=1 
        # heights[i] is >= 0

        # step 3: brute force 
        # find all possible combinations of rectangles using double nested for loop 
        # time complexity of O(n^2)

        # step 4: solution > stack 
        # add each element to the stack 
        # if the element added is greater than, continue adding 
        # create a separate array to store the values greater 
        # area = len(stack) * min(stack)

        stack = []
        # you can store pairs in stack 
        max_area = 0 

        # iterate through index and heights 
        for i, h in enumerate(heights): 
            # have to be able to extend it backwards 
            start = i
            while stack and stack[-1][-1] > h: 
                # since its a pair, we assign a variable to each value 
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                # we set start up to index because we append after 
                start = index
            stack.append([start, h])
        
        for i, h in stack: 
            area = h * (len(heights) - i)
            max_area = max(max_area, area)

        return max_area 