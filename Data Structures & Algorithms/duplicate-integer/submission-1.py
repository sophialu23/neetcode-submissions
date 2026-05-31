class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # step 1: edge cases 
            # no elements in array
        # step 2: constraints 
            # stated in neetcode 
        # step 3: brute force
            # for loop 
        # step 4: how to solve problem 
            # for loop would be simplest with a set 
            # O(n) time
            # O(n) space complexity

        # create a set for all seen values 
        seen = set()

        for n in nums: 
            if n in seen: 
                return True
            else: 
                seen.add(n)
    
        return False 
        
