class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # step 1, 2: edge cases and constraints
        # n is always >= 1 
        # target always greater than positions 

        if len(position) == 1: 
            return 1

        # step 3: brute force solution > two nested for loops 
        # we would have to calculate every possible position and combinations of the cars

        # step 4: solution > stack 
        # we have to check if the differente cars intersect at any point @ or before the destination
        # to do this, we check the time it takes to get to the destination
        # if the car in fronts time is > than the one behind 
        # they collide, and we delete the car behind 
        # add all the cars into a stack and remove the one on top if they collide 
        # the length of the stack will be the total number of car fleets 

        # time complexity > O(nlogn)
        # space complexity O(n)
        # create a pair of position and speed 
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()

        stack = []

        for p, s in pair[::-1]: # reverse sorted order, largest -> smallest 
        # we want to process the cars closest to target first 
            time = (target - p) / s # decimal division 
            stack.append(time)
            # 2 because we append to stack first 
            # 
            if len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
            
        return len(stack)


