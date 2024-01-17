"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Check for empty lists
        if not list1:
            return list2
        if not list2:
            return list1

        # Initialize a dummy node to simplify the code
        dummy = ListNode()
        current = dummy

        # Iterate through both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                # If value in list1 is smaller, append it to the merged list
                current.next = list1
                list1 = list1.next
            else:
                # If value in list2 is smaller or equal, append it to the merged list
                current.next = list2
                list2 = list2.next

            # Move the current pointer to the last node in the merged list
            current = current.next

        # If one list is longer than the other, append the remaining nodes
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list starting from the next of the dummy node
        return dummy.next
