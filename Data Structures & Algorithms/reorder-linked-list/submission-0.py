# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # goal of this problem is to reorder the list grabbing from beggining and end alternating
        # step 1 : edge cases and constraints 
        # what if the list is empty or what if there are only two elements 

        # step 2: clarifying questions 
        
        # step 3: method > slow and fast 
        # two steps to this problem 
        # 1. reverse the second half of the list
        # 2. then alternate between the first and second half. 
        # how to find the middle > slow and fast pointer 
        # move the slow pointer by 1 and fast by 2. do this until the fast reaches the end. 


        slow = head 
        fast = head.next 
        while fast and fast.next: 
            # we do fast and fast.next because fast is jumping twice as fast as slow and we need to ensure that there is always a next one that exists. 
            slow = slow.next 
            fast = fast.next.next
    
        second = slow.next 
        prev = slow.next = None 

        while second: 
            temporary = second.next 
            second.next = prev
            prev = second 
            second = temporary

        first = head 
        second = prev 
        while second: 
            temp1 = first.next 
            temp2 = second.next 
            first.next = second 
            second.next = temp1 
            first, second = temp1, temp2 


