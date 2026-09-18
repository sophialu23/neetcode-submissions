class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # step 1: edge cases and constraints 
        # goal is to return the median of the entire array 
        # are both the arrays always going to have values 
        
        # step 2: clarifying questions 
        # can any of the numbers be negative 
        # assuming there can be multiple duplicates
        
        # step 3: solution > binary search 
        total = len(nums1) + len(nums2)
        half = total //2 
        if len(nums2) < len(nums1): 
            nums1, nums2, = nums2, nums1

        left, right = 0, len(nums1)
        while True: 
            middle = (left + right)//2  # this is the middle for nums1 
            middle2 = half - middle # middle for nums2
            
            left1 = nums1[middle - 1] if middle > 0 else float ("-inf")
            right1 = nums1[middle] if middle < len(nums1) else float("inf")
            left2 = nums2[middle2 -1] if middle2 > 0 else float ("-inf")
            right2 = nums2[middle2] if middle2 < len(nums2) else float("inf")

            if left1 <= right2 and left2 <= right1: 
                # odd 
                if total %2: 
                    return min(right1, right2)
                # even
                return (max(left1, left2) + min(right1, right2)) /2 
            elif left1 > right2: 
                right = middle - 1 
            else: 
                left = middle + 1 
        return 0 
