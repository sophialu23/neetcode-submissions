# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a dictionary to be able to track the visited nodes 
        # if the next node is in the list, move on, otherwise, continue 

        # using a dictionary for quick access. 
        # cant set it to current.val because different nodes might have the same value 
        seen = set()
        current = head 
        while current: 
            if current not in seen: 
                seen.add(current)
            else: 
                return True 
            current = current.next

        return False 
