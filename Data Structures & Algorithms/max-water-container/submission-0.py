class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # step 1, 2: height array is always greater than 2
        # height values cant be negative 

        # step 3: brute force 
        # iterate through the array and find the smallest combination 
        # two nested for loops 
        # time complexity is O(n^2)

        # step 4: solution > two pointers 
        # two pointers, one at zero and one at heights.len -1 
        left = 0 
        right = len(heights) - 1 

        # calculate the max height and store it 
        # now find the min out of the two and move that one 
        # now calcualte the height and store it 
        # if its bigger than max water replace it 
        # continue until left >= right 
        # time complexity O(n)
        # space complexity O(1)

        max_water = 0
        while left < right: 
            area = (right - left)*min(heights[left], heights[right])
            if heights[left] < heights[right]: 
                left += 1 
            elif heights[left] > heights[right]: 
                right -= 1 
            # note: always account for all edge cases
            else: 
                left += 1 

            max_water = max(max_water, area)
            
        return max_water
