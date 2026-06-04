class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            # step 1, 2: edge cases and constraints 
            # length of nums is always greater than 3 
            # not always gaurenteed a solution 

            # step 3: brute force 
            # three nested for loops
            # time complexity O(n^3)
            # space complexity O(1)

            # step 4: solution 
            # cannot contain duplicate triplets and cannot have repeating values 
            # within each triplet 
            # firstly sort the input array and skip all duplicates 
            
            nums.sort() # sort the originals nums array 
            # default of .sort() is always increasing 
            # in a list we append 
            result = []

            # n is the value, must use range 
            # we use minus 2 because if we go beyond that there is no room for 
            # left and right 
            for n in range(len(nums)-2): 
                # if there are two values that are the same 
                # skip the value you have already processed 
                if n > 0 and nums[n] == nums[n-1]: 
                    continue
                left = n+1 
                right = len(nums) -1 
                
                while left < right: 
                    if (nums[left] + nums[right] + nums[n]) == 0: 
                        # append always uses round brackets 
                        result.append([nums[n], nums[left], nums[right]])
                        left += 1 
                        right -= 1 
                        # we could skip after append but there could be multiple valid 
                        # indices with the same n thats why we continue through the loop
                        while left < right and nums[left] == nums[left -1]: 
                            left += 1 
                        while left < right and nums[right] == nums[right +1]: 
                            right -= 1 
                    elif (nums[left] + nums[right] + nums[n]) < 0: 
                        left += 1 
                    elif (nums[left] + nums[right] + nums[n]) > 0:
                        right -= 1 
            
            return result
                        