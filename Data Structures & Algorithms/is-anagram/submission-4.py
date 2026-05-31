class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # step 1: edge cases 
        # string is empty 

        # step 2: constraints > stated

        # step 3: brute force, sorting and compare whether they are the same 
            # time complexity would be O(nlogn)

        # step 4: solution 
            # hash map solution, create a hash map that store all letters of t 
            # time complexity O(n)
            # space complexity O(n)

        # first check if s and t are the same length
        if len(s) != len(t): 
            return False 
        

        # create a hash map 
        count = {}
        # for every character in string s
        for c in s: 
            # add the character to the hashmap and then add how many times it appears 
            count[c] = count.get(c, 0) + 1
        # for every character in string t 
        for c in t: 
            # decrease the character in count
            # note for hashmaps you have to get the values 
            count[c] = count.get(c, 0) - 1
            if count[c] < 0: 
                return False 

        return True 
