class Solution:
    def trap(self, height: List[int]) -> int:
        # step 1, 2: edge cases and constraints 
        # heights array is always greater than = to 1 
        # heights values are always greater than = to 0 
        
        # step 3: brute force 
        # find all possible traps 
        # brute force, going through all possible traps 
        # time complexity O(n^2)

        # step 4: solution > two pointers 
        # have a pointer for farthest left and farthest right 
        # create a variable for max left, right
        # find the smallest value and shift it 
        # min(left, right) - height[i]

        left = 0 
        right = len(height) - 1

        max_left = height[left] 
        max_right = height[right] 

        # this keeps track of the total rainwater 
        result = 0 

        while left < right:
            if max_left <= max_right: 
                left += 1 
                # we must update max left 
                max_left = max(max_left, height[left])
                # only need to account for one side at a time 
                rainwater = max_left - height[left]
                # you have to update result each time 
                result += rainwater 
            elif max_left > max_right: 
                right -= 1 
                max_right = max(max_right, height[right])
                rainwater = max_right - height[right]
                result += rainwater
        return result