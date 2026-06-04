class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       # step 1, 2: edge cases and constraints 
       # no additional space 
       # length of nums always greater than or = 2 
       # sorted in increasing order 

       # step 3: potential solutions
       # have two pointers on farthest left and farthest right 
       # while they do not cross each other 
       # check if its bigger than or smaller than target and adjust accordingly
       # since nums is sorted 
       # time complexity O(n)
       # space complexity O(1)

       # its .len in pytho 
       left = 0 
       right = len(numbers) -1

       while left < right: 
        if (numbers[left] + numbers[right]) == target: 
            return [left+1, right+1]
        elif (numbers[left] + numbers[right]) < target: 
            left += 1
        elif (numbers[left] + numbers[right]) > target: 
            right -= 1 

        