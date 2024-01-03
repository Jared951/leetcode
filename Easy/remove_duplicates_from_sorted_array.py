"""
Given an integer array nums sorted in non-decreasing order(non-decreasing = ascending), 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize a variable to keep track of the new length of the array
        l = 1

        # Iterate through the array starting from the second element, since the array is always in ascending 
        for r in range(1, len(nums)):
            # Check if the current element is different from the previous one
            if nums[r] != nums[r-1]:
                # If different, update the next position in the array with the current element
                nums[l] = nums[r]
                # Increment the new length variable
                l += 1

        # Return the new length of the array with duplicates removed
        return l

# Given array        
input_array = [0,0,1,1,1,2,2,3,3,4]

# Create an instance of the Solution class
solution_instance = Solution()

# Call the removeDuplicates method to modify the array in-place
result = solution_instance.removeDuplicates(input_array)

# print the amount of values in the array
print(result)

# print the array 
print(input_array[:result])

"""
Run time: 57 ms
Memory: 14.9 MB
O(n)
"""