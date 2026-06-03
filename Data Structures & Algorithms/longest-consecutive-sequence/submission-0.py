class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # step 1, 2: edges and constraints 
        # nums is always bigger than 0 
        
        # step 3: brute force 
        # O(nlogn) sorting and check if whether its consecutive  

        # step 4: solution 
        # create isolated sequences for values that are beside eachother 
        # to find if a number is the beginning of a sequence convert the array to a set 
        # and then check the set to find if the n-1 exist 
        # time O(n)
        # space complexity O(n)

        # set (), tuple (), array [], dict {} 
        seen = set(nums)
        longest = 0
        for n in nums: 
            # check if its the start of a sequence 
            if (n-1) not in seen: 
                # create a variable for length to keep track 
                length = 0 
                # while the next consecutive number is in the set 
                while (n+length) in seen: 
                    # add it to the length 
                    # so it would ne n+1, then n+2, etc. 
                    length += 1 
                # take the longest out of current length and previous longest 
                longest = max(length, longest)
        return longest 

            
        

       