"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a variable k to track the position where non-val elements are placed in the list.
        k = 0 

        # Iterate through each element in the input list nums.
        for i in range(len(nums)):
            # Check if the current element nums[i] is not equal to the specified value val.
            if nums[i] != val:
                # If true, update the value at position k in nums with the current element nums[i].
                nums[k] = nums[i]
                # Increment k to prepare for the next non-val element.
                k += 1
        
        # After iterating through the entire list, return the value of k, representing the length of the modified list without val.
        return k

# nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
solution = Solution()
result = solution.removeElement([3, 2, 2, 3], 3)
print("Length of modified nums array:", result)

# Runtime: 19 ms,  Memory: 13.2 MB, Time Complexity: 0(n)