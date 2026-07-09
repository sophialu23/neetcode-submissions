class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # step 1, 2: edge cases and constraints 
        # piles length is >= 1 
        # h is always greater than piles length 
        # pile[i] >= 1 
        
        # step 3: brute force solution > trying all possible k until 
        # you find one below h 

        # step 4: solution > binary search 
        # number of hours is always gonna start at the largest value in the array 
        # and then cut down from there 

        least = 1 
        max_num = max(piles)
        result = max_num # worst case possible 

        if len(piles) == h: 
            return max_num

        while least <= max_num: 
            middle = (least + max_num) // 2
            # calculate hours needed at speed mid 
            hours = 0 
            for i in piles: 
                hours += math.ceil(i / middle)
                
            if hours > h: 
                least = middle + 1 
            elif hours <= h: 
                max_num = middle - 1 
                result = middle 
        return result 


