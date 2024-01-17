"""
Design your implementation of the linked list. 
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. 
val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
 

Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""
class ListNode:
    def __init__(self, val):
        # Node constructor, initializes a node with a given value
        self.val = val
        self.prev = None  # Reference to the previous node
        self.next = None  # Reference to the next node

class MyLinkedList(object):

    def __init__(self):
        # Linked list constructor, initializes an empty linked list with dummy head and tail nodes
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index): 
        # Get the value of the node at a given index in the linked list
        current = self.head.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and current != self.tail and index == 0:
            return current.val
        return -1

    def addAtHead(self, val): 
        # Add a node with a given value at the beginning of the linked list
        new_node, next_node, prev_node = ListNode(val), self.head.next, self.head
        prev_node.next = new_node
        next_node.prev = new_node
        new_node.next = next_node
        new_node.prev = prev_node

    def addAtTail(self, val): 
        # Add a node with a given value at the end of the linked list
        new_node, next_node, prev_node = ListNode(val), self.tail, self.tail.prev
        prev_node.next = new_node
        next_node.prev = new_node
        new_node.next = next_node
        new_node.prev = prev_node

    def addAtIndex(self, index, val): 
        # Add a node with a given value at a specified index in the linked list
        current = self.head.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and index == 0:
            new_node, next_node, prev_node = ListNode(val), current, current.prev
            prev_node.next = new_node
            next_node.prev = new_node
            new_node.next = next_node
            new_node.prev = prev_node

    def deleteAtIndex(self, index):
        # Delete the node at a specified index in the linked list
        current = self.head.next
        while current and index > 0:
            current = current.next
            index -= 1
        if current and current != self.tail and index == 0:
            next_node, prev_node = current.next, current.prev
            next_node.prev = prev_node
            prev_node.next = next_node
