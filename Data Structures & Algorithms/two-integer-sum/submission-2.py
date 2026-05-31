class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # step 1: edge cases > array is empty, early exit, array has one value 
        # step 2: constraints > 1 pair only 
        # step 3: brute force > 2 nested for loops to be able to go through each value pairing 
            # time complexity would be O(n^2)
            # space complexity would be O(1)
        # step 4: optimized solution > hashmap 
            # solution 1: sort the values and then have two pointers
            # solution 2: hashmap, go through every value in the array 
            # and then check if the target minus that value in the array exist 
            # if the value exist, then we return the index, if it does not add current 
            # value where we are checking into the hashmap 
            # time complexity: O(n) > worst case go through entire array 
            # space complexity: O(n)
       
       # initialize the hashmap
       # edge cases


        seen = {}

        # iterate through the array 
        # n is the value 
        # enumerate gives you both the value and the index instead of just one 
        for i, n in enumerate(nums): 
            if target - n not in seen: 
                seen[n] = i
            else:   
                return [seen[target-n], i]

