class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # step 1, 2: edge cases and constraints 
        # nums length is greater than =>1 
        
        # step 3: brute force approach > find the max in each k window 
        # time complexity would be O(k*(n-k))

        
        # step 4: solution > sliding window approach, dequeue solution
        # create a queue with the max in the current value 
        # and then as we shift the window right, we compare each new value to the current max 
        # insert it into the array 
        # the window is k sized 
        # adding and removing is O(1) time 

        # this apporach is called a monotonic decreasing queue 
        # before adding new index, we pop from the back of the queue 
        # add the current index 
        # remove the front if that index has fallen out of k window 
        # the front of the queue will always be the max  
        
        left = 0 
        max_num = []
        queue = deque()

        for right in range(len(nums)): 
            # remember indices of arrays always start at 0 
            # the back of the queue will always hold the smallest values
            # compare new potential added index
            while queue and nums[queue[-1]] < nums[right]: 
                queue.pop()

            # add the new items 
            queue.append(right)

            # get rid of old not valid index 
            if queue[0] < left: 
                queue.popleft()
            
            if right - left + 1 == k: 
                # queue stores indexes not values 
                max_num.append(nums[queue[0]])
                left += 1 

        return max_num


