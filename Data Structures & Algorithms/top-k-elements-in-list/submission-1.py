class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1: edge cases > nums is empty NA 
        # step 2: constraints > nums is always greater than 1 

        # step 3: brute force approach > count each value in the hashmap 
        # sort the frequency of each value 
        # return the top k elements 
        # go through the array and create a key for each new number
        # the value would be the number of times it appears 
        # time complexity would be O(nlogn)
        # space complexity would be O(n)

        # step 4: the most optimal way 
        # the most optimal way is > bucket sort 
        # hash map that has the count as the key and the value as the number 
        # then we could find the top k elements going from the last element until top k 
        # time complexity is O(n)
        # space complexity is O(n)

        # create a hash map 
        # key value pair of value and frequency
        count = {}

        # iterate through array 
        for n in nums: 
            count[n] = 1 + count.get(n, 0)

        # sort the count in decsending order 
        # sorting count, with the key not the alphabetical order count[x], and set revrse to true 
        count = sorted(count, key= lambda x: count[x], reverse = True) 
        return count[:k]

