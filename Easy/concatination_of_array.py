"""
Given an integer array nums of length n, 
you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""

class Solution(object):
    def getConcatenation(self, nums):
         # Initialize an empty list named 'ans' to store the result
        ans = []

        # Iterate twice to concatenate 'nums' array with itself
        for i in range(2):
            # Iterate through each element in the 'nums' array
            for n in nums:
                # Append the current element 'n' to the 'ans' list
                ans.append(n)
        
        # Return the concatenated array 'ans'
        return ans

solution_instance = Solution()

nums1 = [1, 2, 1]
result = solution_instance.getConcatenation(nums1)
print(result)

# O(n), Runtime 55 ms, Memory 13.7 MB