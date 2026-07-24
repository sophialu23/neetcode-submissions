class Solution:
    def search(self, nums: List[int], target: int) -> int:
         # step 1, 2: edge cases and constraints 
         # length of nums is >= 1 
         # all values of nums are unique 
         
        if len(nums) == 1: 
            if target == nums[0]: 
                return 0
            else: 
                return -1 

        # step 3: brute force O(n) time 
        # iterate through the entire array and find target 

        # step 4: solution > binary search 
        # we need to determine if the middleis in the left or right side 
        # and then we have to find if target is higher than or lower than middle 

        left = 0 
        right = len(nums) - 1 

        while left <= right: 
            middle = (left + right) // 2 # integer division 
            if target == nums[middle]: 
                return middle 
            # check which sorted portion we are in 
            # left sorted portion of the array
            if nums[middle] >= nums[left]: 
                if target > nums[middle] or target < nums[left]: 
                    left = middle + 1 
                else: 
                    right = middle -1 
            # right sorted portion of the array 
            else: 
                if target < nums[middle] or target > nums[right]: 
                    right = middle - 1 
                else: 
                    left = middle + 1 
                
        return -1 
        
        