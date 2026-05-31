class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # step 1: edge cases, the string is empty only one value 
        # step 2: constraints only made up of lowercase letters 
        # this means no need to toLower all characters 

        if len(strs) == 0: 
            return [] 
        if len(strs) == 1: 
            return [strs]

        # step 3: brute force, go through each character of each strs and store it and compare all strings 
        # go through multiple times 
        # time complexity would be O(n^2)
        # space complexity would be O(n)

        # step 4: optimal solution > sorting each string and store in hashmap 
        # the key value pair would be the string and then the original string 
        # then it would return the orginal string of all keys that are the same 

        # create a hashmap 
        # create a list for the hashmap as each string would be mapped to an appending list 
        # default dict is a type of hashmap that maps every key to a list instead of a singular value 
        strings = defaultdict(list)

        # create a for loop to iterate through all the strings 
        for s in strs: 
            # create the key to be a sorted tuple, sorting as we iterate through the array 
            key = tuple(sorted(s))
            # for each key append the value at s, the original string 
            strings[key].append(s)

        # return all the values in the hashmap in the form of a list 
        # list of all keys, with list of all values embededded within 
        # list already creates [] so no need to wrap in [] 
        # string.values is a call 
        return list(strings.values())
