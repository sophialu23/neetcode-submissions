class Solution:
    # step 1: edge cases, string is always greater than 0 
    # step 2: constraints, already considered in the problem 

    # step 3: brute force > NA
    # step 4: solution, since it includes the library
    # map each letter to the coressponding position in the alphabet, ie. A would be 1 
    # create a hashmap with all letters as the key and all numbers as the values 
    # iterate through the string and find each coressponding value and then store it in a new s

    # first solution wont work
    # second solution > before each word have how many letters there are in the word 
    # and then have delimeter 
    # a delimeter is a way to tell how one thing ends and another thing starts 


    def encode(self, strs: List[str]) -> str:
        # initialize the results 
        res = ""
        for s in strs: 
            res += f"{len(s)}#{s}" # f"" is basically a string that lets you embed variables inside a string
        # returns the encoded strings 
        return res 

    def decode(self, s: str) -> List[str]:
        # store the results in an array 
        res = [] 
        i = 0
        while i < len(s): 
            j = i 
            while s[j] != "#": 
                j += 1 
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 + length 
        
        return res 

