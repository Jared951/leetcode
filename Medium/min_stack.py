"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack(object):
    # Initializing the MinStack class with two separate stacks for values and minimums
    def __init__(self):
        self.stack = []      # Stack to store elements
        self.minStack = []   # Stack to store the minimum element at each level

    # Function to push an element onto the stack
    def push(self, val):
        self.stack.append(val)  # Adding the element to the main stack
        # Calculating the minimum value between the current element and the minimum value at the previous level
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)  # Adding the minimum value to the minStack

    # Function to pop the top element from both stacks
    def pop(self):
        self.stack.pop()      # Removing the top element from the main stack
        self.minStack.pop()   # Removing the corresponding minimum value from the minStack

    # Function to get the top element of the main stack
    def top(self):
        return self.stack[-1]

    # Function to retrieve the minimum element in the stack
    def getMin(self):
        return self.minStack[-1]
