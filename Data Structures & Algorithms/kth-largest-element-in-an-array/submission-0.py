class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time complexities for heaps are always O(logn)

        # step 1: edge cases and constraints 
        # what if nums is empty or what if nums only has one number 
        if len(nums) == 0: 
            return 0 
        if len(nums) == 1: 
            return nums[0]

        # step 2: solution approach 
        # using a heap to continuously find the max 
        # once we create a heap we will continue to pop k times 
        # because its askin for the elements in sorted order and not the kth distinct element 
        # if we pop k times, we will get the correct answer 
        heap = [-n for n in nums] # add all n in nums and negate it
        heapq.heapify(heap) # heapify it 

        for i in range(k-1): 
            heapq.heappop(heap)

        return -heap[0]