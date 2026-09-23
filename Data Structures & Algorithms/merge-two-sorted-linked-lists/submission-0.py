# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # step 1: edge cases and constraints 
        # what if one of the list are empty 
        # there is no such thing as checking the len of a list like an array 

        # step 2: clarifying questions 
        # can there be duplicates in lists 
        # can the values in the list be negative 

        # step 3: solution
        # we can compare each value of the two list at head 
        # always append to the list the one that is the least 
        
        starter = ListNode(0)
        current = starter 
        while list1 and list2: 
            # note: in python, for linkedlist you must call the value by val 
            if list1.val <= list2.val: 
                current.next = list1
                current = current.next 
                list1 = list1.next
            else: 
                current.next = list2
                current = current.next 
                list2 = list2.next
        
        if list1: # this means this is true while list 1 still points to a node  
            current.next = list1
            list1 = list1.next
        if list2: 
            current.next = list2
            list2 = list2.next

        return starter.next # must do next because starter will always be fixed 
        # this is how you start the list off 
        