class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a dictionary for stored values of seen sets 
        last_seen = {}
        left = 0
        max_length = 0 

        # iterate through array 
        # use right as a sliding window 
        for right in range(len(s)): 
            # if the value at right is in set last_seen and the index of the 
            # repeated value is bigger or = to left, you move to left to the repeated value 
            # removing duplicates 
            if s[right] in last_seen and last_seen[s[right]] >= left:  
                left = last_seen[s[right]] + 1

            # set the repeated value index to right 
            # this would mean the last element would be the repeated value 
            last_seen[s[right]] = right
            # get the max length, the right - left + 1 which is size 
            max_length = max(max_length, right - left + 1)


        return max_length