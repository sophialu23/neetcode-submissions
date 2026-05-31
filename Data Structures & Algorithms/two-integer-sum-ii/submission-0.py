class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # create two pointers, one to end and one at beginning
        right = len(numbers) - 1 
        left = 0 

        while left < right: 
            current_sum = numbers[left] + numbers[right]

            if current_sum == target: 
                return [left +1, right+1]
            
            if current_sum > target: 
                right -= 1

            if current_sum < target: 
                left += 1
       