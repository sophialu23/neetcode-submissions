class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # step 1, 2: edge cases and constraints 
        # length of s >= 1 
        # k can be >= 0 

        # step 3: brute force approach
        # with sliding windows and two pointers, the brute force is always 2 nested for loops 
        # iterate through the array with two nested for loop 
        # checking every possible longest string and replacing it 
        # time complexity O(n^2)

        # step 4: solution > sliding window approach 
        # have a left bound counting the character and right moving forward
        # if you encounter a letter that is not the same, replace it if possible 
        # then keep counting until you run out of k letters 
        # continue until you get rid of all k letters 
        # create a hashmap to keep count of all character occurances 
        # time complexity O(n)
        # space complexity of O(n) > hash maps take up O(n)

        left = 0 
        max_string = 0 
        count = {} 

       # right is the index 
        for right in range(len(s)): 
            # add the count of new character to hashmap  
            if s[right] in count: 
                count[s[right]] += 1 
            else: 
                count[s[right]] = 1

            # take the least counted value in hashmap 
            most = max(count.values())

            # continue until you no longer can 
            # have to do + 1 since indexed 0 
            if (right - left) + 1 - most > k: 
                # you never manually move right
                count[s[left]] -= 1
                left += 1
            else: 
                # find the current window 
                current_max = right - left + 1
                max_string = max(current_max, max_string)
        
        return max_string 
        

         
        
