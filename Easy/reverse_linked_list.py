"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative solution Time: O(n) Memomry:0(1) 
class Solution(object):
    # Method to reverse a linked list
    def reverseList(self, head):
        # Initialize 'previous' to None as there is no node before the head initially
        previous = None
        # 'current' starts with the head of the linked list, set it equal 
        current = head

        # Iterate through the linked list until 'current' becomes None (end of the list)
        while current:
            # Save the next node in the original list to 'nxt'
            nxt = current.next
            # Reverse the link by pointing 'current.next' to the 'previous' node
            current.next = previous
            # Move 'previous' and 'current' pointers one step forward in the linked list
            previous = current
            current = nxt
        
        # Return the new head of the reversed linked list (which is now 'previous')
        return previous
