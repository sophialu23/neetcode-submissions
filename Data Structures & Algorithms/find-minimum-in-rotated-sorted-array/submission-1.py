class Solution:
    def findMin(self, nums: List[int]) -> int:
        #step 1, 2: edge cases and constraints
        # length of nums is >= 1 
        # edge cases, rotate = len of array 

        # step 3: brute force > for loop 
        # iterate through every element in the array and return minimum

        # step 4: binary search
        # we have to find if the middle is in the right or left portion 
        # if nums[m] >= nums [l]
        
        left = 0 
        right = len(nums) - 1 
        result = nums[0]

        while left <= right: 
            if nums[left] < nums[right]: 
                result = min(result, nums[left])
                break
            middle = (left + right) // 2 # integer division
            result = min(result, nums[middle])
            if nums[middle] >= nums[left]: 
                left = middle + 1 
            else: 
                right = middle - 1 
            
        return result 

