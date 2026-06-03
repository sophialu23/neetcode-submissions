class Solution:
    def isPalindrome(self, s: str) -> bool:
        # step 1, 2: constraints and edge cases 
        # length of original string is greater or = to 1 

        if len(s) == 1: 
            return True 

        # step 3: brute force 
        # loop through the array 
        # creating another array but flipped backwards and compare to current array 

        # step 4: solution 
        # have a left and right pointer 
        # compare the two until they are = 

        left = 0 
        right = len(s) - 1 
         
        while left < right: 
            # isalnum() checks if the char is alphanumeric 
            # you have to have the inner left < right check 
            # because the outside one is the main one 
            # checking overall, but for example if you encounter multiple spaces in a row 
            # left could overpass right 
            while left < right and not s[left].isalnum(): 
                left += 1 
            while left < right and not s[right].isalnum(): 
                right -= 1
            # you have to lower each of the chars using .lower()
            if s[left].lower() != s[right].lower(): 
                return False 
            
            left += 1 
            right -= 1

        return True 