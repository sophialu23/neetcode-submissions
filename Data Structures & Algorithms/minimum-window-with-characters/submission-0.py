class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # step 1, 2: edge cases and constraints 
        # one possibility is that t > s 

        if len(t) > len(s): 
            return ""
        
        # step 3: brute force approach 
        # check every possible combination of strings 
        # two nested for loops > O(n^2)

        # step 4: solution 
        # sliding window approach 
        # have a left pointer and then a min substring value 

        # create a hash map for all values in t 
        seen = {} 
        # cannot reuse the parameter s 
        # if i do in t then its all the values in t rather than index 
        for char in t: 
            # add one to value of s if not 0 add one 
            seen[char] = seen.get(char, 0) + 1 

        # create a hashmap with s 
        # create a hashmap with t 
        # continuously compare to see if it is the same or greater 
        # do that until the condition is met then get ths string size 
        # add one to left and update the hashmap of s 
        
        # this is the window of s 
        window = {}
        # we have to create the values of have and need 
        have, need = 0, len(seen)

        left = 0 
        min_substring = float('inf') # if you are finding the min, always set inital value to inf 
        result = "" # return a string

        for right in range(len(s)): 
            # add one to the window for 
            window[s[right]] = window.get(s[right], 0) + 1 
            # we need to do window[s[right]] to account for the number of characters 
            # not just the characters themselves
            if s[right] in seen and window[s[right]] == seen[s[right]]: 
                have += 1 
            
            while have == need: 
                # we only update if its less than min_substring 
                if right - left + 1 < min_substring: 
                    # this is the notation for creating a string 
                    # from left to right + 1 
                    # always one less than right outer bound 
                    result = s[left:right+1]
                    # we cannot compare int and strings 
                    min_substring = right - left + 1 
              
                if window[s[left]] != 0: 
                    window[s[left]] -= 1
                
                # must also substract one from have 
                if s[left] in seen and window.get(s[left],0) < seen[s[left]]: 
                    have -= 1

                # window.get(s[left],0) returns 0 if key does not exist
                # we cant completely delete the character before we check if its in seen and -1 from have 
                if window.get(s[left],0) == 0: 
                    # there is no delete in python, only del 
                    del window[s[left]]
 
                left += 1  
            
        return result

       