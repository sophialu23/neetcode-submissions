class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # step 1, 2: edge cases and constraints 
        # lengths of s1, 2 always >= 1 

        # step 3: brute force approach 
        # go through every possible combination 
        # two nested for loops

        # step 4: solution > sliding window + hashmap 
        # keep track of all the letters in s1 
        # sliding window approach for s2

        # edge case where s1 is larger 
        if len(s1) > len(s2): 
            return False 

        seen = {}

        # this is the value s, the last value 
        # if i use range, that is the index s 
        for s in range(len(s1)): 
            if s1[s] in seen: 
                seen[s1[s]] += 1 
            else: 
                seen[s1[s]] = 1
        
        left = 0 
        # create another set for s2 
        count_window = {} 
        
        # right is the index 
        for right in range(len(s2)): 
            count_window[s2[right]] = count_window.get(s2[right], 0) + 1
            # if the window is bigger than s1 
            if right - left + 1  > len(s1): 
                # remove a count from left character 
                count_window[s2[left]] -= 1 
                # if the character count is 0 now
                if count_window[s2[left]] == 0: 
                    # delete it from count window 
                    del count_window[s2[left]]
                    # move left forward
                left += 1  
            
            if count_window == seen: 
                return True 

        return False 

