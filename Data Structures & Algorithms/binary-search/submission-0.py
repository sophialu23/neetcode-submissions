class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # step 1, 2: edge cases and constraints 
        # len of nums >= 1 

        # step 3: brute force 
        # for loop iterating through entire array 

        # step 4: solution > binary search 
        # have the left pointer and right pointer, add them together/2 
        # since the input array is sorted, we compare target if larger or smaller and then repeat 
        # time complexity > O(logn)

        left = 0 
        right = len(nums) - 1 # index of array 
        while left <= right: 
            middle = (left + right) // 2 # integer division 
            if nums[middle] == target: 
                return middle 
            elif nums[middle] > target:
                right = middle - 1 
            elif nums[middle] < target: 
                left = middle + 1 
        
        return -1




        