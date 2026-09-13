class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # step 1: edge cases and constraints 
        # so num is always larger than two 
        
        # step 2: clarifying questions 
        # is it possible to have duplicates in the array 
        # is it possible to have negatives in the array 
        # is nums always sorted > assume no

        # step 3: solution 
        # create a hahsmap with index and number
        # iterate through nums and for every nums find if that value - target is in seen 
        # if not then continue 
        # if yes then append to result [index at n, index in hashmap]

        seen = {} 
        for i, value in enumerate(nums): 
            search = target - value 
            if search in seen:
                return [seen[search], i]
            seen[value] = i 