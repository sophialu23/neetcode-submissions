# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list: you cant approach the same way as an array 
        # create two variables holding for current and the prev 

        prev = None
        current = head 

        # create a loop that state that while current does not reach the end 
        while current: 
            next_node = current.next # save the next node 
            current.next = prev # reverse the linked list set the newest element to prev
            prev = current # set new prev 
            current = next_node # move current forward 

        return prev
