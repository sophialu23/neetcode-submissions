class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # edge cases nums length is always greater than 2 
        # solve in O(n) time complexity 

        # step 3: brute force 
        # loop through the array to ensure every number is touched 

        # step 4: solution 
        # postfix/ prefix solution
        # we create two arrays for all product to the left of a number and all product to right of a number 
        # this is an O(n) time because going through array twice is just 
        # O(n) + O(n) which is till O(n)
        # space complexity would be O(n) because same length as the array itself 
        # then we times the two arrays 

        # (start, stop, step)
        # start at the last index of nums, stop before -1 which is 0 
        # step move backwards 
        postfix = 1
        # create an array for all products to right 
        right = [1] * len(nums) 
        # for numbers in range length of nums 
        for n in range(len(nums)-1, -1, -1): 
            # multiple the number at index n with postfix 
            right[n] *= postfix 
            # multiple postfix with the number at n
            postfix *= nums[n]

        # repeat the same process for all numbers to the left
        prefix = 1
        left = [1] * len(nums)
        # stop before len(nums) which would be len(nums)-1
        for n in range(0, len(nums), 1): 
            left[n] *= prefix 
            prefix *= nums[n]

        # multiple the two arrays together 
        output = [1] * len(nums)
        # when you just do output, n gives you the values not the indexes of the values 
        for n in range(len(output)):  
            output[n] = right[n]* left[n]
        
        return output 
        
            