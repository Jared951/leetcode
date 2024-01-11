"""
You are keeping the scores for a baseball game with strange rules. 
At the beginning of the game, 
you start with an empty record.

You are given a list of strings operations, 
where operations[i] is the ith operation 
you must apply to the record and is one of the following:

An integer x. - Record a new score of x.
'+'. - Record a new score that is the sum of the previous two scores.
'D'. - Record a new score that is the double of the previous score.
'C'. - Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

 

Example 1:

Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.

Example 2:

Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.

Example 3:

Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
 

Constraints:

1 <= operations.length <= 1000
operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
For operation "+", there will always be at least two previous scores on the record.
For operations "C" and "D", there will always be at least one previous score on the record.


This is a STACK
C = Pop from stack
D = Double the previous score
+ = add the stack
"""

class Solution(object):
    def calPoints(self, operations):
        # Initialize an empty stack to keep track of scores
        stack = []

        # Iterate through each operation in the input list
        for op in operations:
            # If the operation is "+", add the sum of the last two scores to the stack
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            # If the operation is "D", double the last score and add it to the stack
            elif op == "D":
                stack.append(2 * stack[-1])
            # If the operation is "C", remove the last score from the stack
            elif op == "C":
                stack.pop()
            # If the operation is an integer, convert it to an integer and add it to the stack
            else:
                stack.append(int(op))

        # Return the sum of all the scores in the final stack
        return sum(stack)

# Example usage
ops1 = ["5", "2", "C", "D", "+"]

# Create an instance of the Solution class
sol = Solution()

# Call the calPoints method with the list of operations and print the result
print(sol.calPoints(ops1))  # Output should be 30
    
# O(n) Runtime: 24ms Memory: 13.70 MB