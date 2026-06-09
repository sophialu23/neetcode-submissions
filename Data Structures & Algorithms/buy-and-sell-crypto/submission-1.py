class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # step 1, 2: edge cases and constraints 
        # prices length is >= 1 
        # price values always >= 0 

        # step 3: brute force solution 
        # iterate through the array with a nested for loop to see which combination of numbers 
        # give you the highest based off order 
        # time complexity of O(n^2)

        # step 4: solution > sliding window approach 
        # the difference between sliding window and two pointers 
        # two pointers start on different sides, sliding > right = left + 1  
        # use a sliding window and determine and keep moving left pointer 
        # until left + 1 > left 
        # and then move right until you reach max 

        # to create a sliding window 
        # begin by initializing left and your variable 
        left = 0 
        max_profit = 0

        # iterate through the rest of the array using right
        for right in range(len(prices)): 
            if prices[right] <= prices[left]: 
                left = right  
            profit = prices[right] - prices[left]   
            max_profit = max(profit, max_profit)

        return max_profit
       
             