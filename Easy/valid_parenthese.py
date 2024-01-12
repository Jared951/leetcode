"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        # Initialize an empty list called 'stack' to keep track of open brackets
        stack = []
        # Create a dictionary 'closeToOpen' mapping each closing bracket to its corresponding open bracket
        closeToOpen = { ")":"(", "]":"[", "}":"{" }

        # Iterate through each character in the input string 's'
        for c in s:
            # Check if the current character is a closing bracket
            if c in closeToOpen:
                # Check if the 'stack' is not empty and the last element in 'stack' matches the corresponding open bracket
                if stack and stack[-1] == closeToOpen[c]:
                    # Pop the last element from 'stack' if conditions are met
                    stack.pop()
                else:
                    # Return False if the conditions are not met, indicating an invalid string
                    return False
            else:
                # If the current character is an open bracket, push it onto the 'stack'
                stack.append(c)

        # Return True if 'stack' is empty, indicating a valid string; otherwise, return False
        return True if not stack else False

# Create an instance of the Solution class
solution_instance = Solution()
# Test the isValid method with an example input and print the result
print(solution_instance.isValid("()"))

